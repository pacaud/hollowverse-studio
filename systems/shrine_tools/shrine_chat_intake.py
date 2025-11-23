from flask import Flask, request, jsonify
import os
import datetime
import re
import pathlib

VAULT_ROOT = "/srv/vault_of_memories_git"
CHAT_BASE = os.path.join(VAULT_ROOT, "shrine_of_memories", "chat_logs", "by_date")

AUTH_TOKEN = os.environ.get("SHRINE_CHAT_TOKEN")

ALLOWED_EXTENSIONS = {".md", ".markdown", ".yaml", ".yml", ".txt", ".json"}
MAX_FILE_SIZE_KB = 512  # safety: don't send huge files

app = Flask(__name__)


def slugify(text: str, max_len: int = 40) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    if not text:
        return "chat"
    return text[:max_len].strip("-")


@app.route("/api/log_chat", methods=["POST"])
def log_chat():
    if AUTH_TOKEN:
        header_token = request.headers.get("X-Auth-Token")
        if header_token != AUTH_TOKEN:
            return jsonify({"error": "unauthorized"}), 401

    data = request.get_json(silent=True) or {}

    title = data.get("title") or "Untitled chat"
    gpt_name = data.get("gpt_name") or "unknown"
    content = data.get("content") or ""
    tags = data.get("tags") or []

    if not content.strip():
        return jsonify({"error": "content is required"}), 400

    today = datetime.date.today().isoformat()
    date_dir = os.path.join(CHAT_BASE, today)
    os.makedirs(date_dir, exist_ok=True)

    gpt_slug = slugify(gpt_name, max_len=20)
    title_slug = slugify(title, max_len=50)
    filename = f"{today}__{gpt_slug}__{title_slug}.md"
    filepath = os.path.join(date_dir, filename)

    fm_lines = [
        "---",
        f"date: {today}",
        f"gpt_name: {gpt_name}",
        f"title: {title}",
    ]
    if tags:
        fm_lines.append("tags:")
        for t in tags:
            fm_lines.append(f"  - {t}")
    fm_lines.append("---")
    fm_lines.append("")

    frontmatter = "\n".join(fm_lines)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write("\n")
        f.write(content.rstrip() + "\n")

    rel_path = os.path.relpath(filepath, VAULT_ROOT)
    return jsonify({"ok": True, "file": rel_path}), 201


@app.route("/api/get_vault_file", methods=["GET"])
def get_vault_file():
    # Auth check (reuse same token)
    if AUTH_TOKEN:
        header_token = request.headers.get("X-Auth-Token")
        if header_token != AUTH_TOKEN:
            return jsonify({"error": "unauthorized"}), 401

    rel_path = request.args.get("path", "").strip()
    if not rel_path:
        return jsonify({"error": "missing path parameter"}), 400

    # Prevent sneaky paths like ../../etc/passwd
    normalized = os.path.normpath(rel_path)
    if normalized.startswith("..") or normalized.startswith("/"):
        return jsonify({"error": "invalid path"}), 400

    full_path = os.path.normpath(os.path.join(VAULT_ROOT, normalized))

    # make sure we stay inside the vault
    if not full_path.startswith(os.path.normpath(VAULT_ROOT)):
        return jsonify({"error": "path escapes vault root"}), 400

    if not os.path.exists(full_path) or not os.path.isfile(full_path):
        return jsonify({"error": "file not found", "path": normalized}), 404

    ext = pathlib.Path(full_path).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        return jsonify({"error": "file type not allowed", "ext": ext}), 400

    size_kb = os.path.getsize(full_path) / 1024.0
    if size_kb > MAX_FILE_SIZE_KB:
        return jsonify({"error": "file too large", "size_kb": size_kb}), 400

    with open(full_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    return jsonify({
        "ok": True,
        "path": normalized,
        "ext": ext,
        "size_kb": size_kb,
        "content": content
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("SHRINE_CHAT_PORT", "5001"))
    app.run(host="0.0.0.0", port=port)

