from flask import Flask, request, jsonify
import os
import datetime
import re

VAULT_ROOT = "/srv/vault_of_memories_git"
CHAT_BASE = os.path.join(VAULT_ROOT, "shrine_of_memories", "chat_logs", "by_date")

AUTH_TOKEN = os.environ.get("SHRINE_CHAT_TOKEN")

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
    # Debug: print what token the server has, and what came in
    print("AUTH_TOKEN on server:", AUTH_TOKEN)
    print("Incoming headers:", dict(request.headers))

    if AUTH_TOKEN:
        header_token = request.headers.get("X-Auth-Token")
        if header_token != AUTH_TOKEN:
            print("Header token mismatch:", header_token)
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


if __name__ == "__main__":
    port = int(os.environ.get("SHRINE_CHAT_PORT", "5001"))
    app.run(host="0.0.0.0", port=port)
