# Voxia Dataflow Server (Nested API + Live Schema Route)
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os, yaml, zipfile, logging
from datetime import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)

LOG_DIR = "/var/log/voxia"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(filename=os.path.join(LOG_DIR, "dataflow.log"),
                    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

API_KEY = os.environ.get("VOXIA_DATAFLOW_TOKEN", "uG2j48nRz7!mA@pF9xQvT1yCwK5oS")

def require_api_key(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.headers.get("X-API-Key") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper

BASE_PATH = "/var/www/dataflow.hollowverse"
DATA_PATH = os.path.join(BASE_PATH, "data")
ARCHIVE_PATH = os.path.join(BASE_PATH, "archives")
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(ARCHIVE_PATH, exist_ok=True)

@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "source": "voxia-dataflow"})

# ------------------ DATA ROUTES ------------------ #
@app.route("/dataflow/data/post", methods=["POST"])
@require_api_key
def post_data():
    if "file" in request.files:
        f = request.files["file"]
        f.save(os.path.join(DATA_PATH, f.filename))
        return jsonify({"status": "success", "message": f"File '{f.filename}' uploaded"})
    if request.is_json:
        data = request.get_json()
        fn = data.get("filename", f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(os.path.join(DATA_PATH, fn), "w", encoding="utf-8") as fp: fp.write(str(data))
        return jsonify({"status": "success", "message": f"JSON saved as '{fn}'"})
    return jsonify({"status": "error", "message": "No data"}), 400

@app.route("/dataflow/data/get/<path:filename>")
@require_api_key
def get_data(filename):
    fp = os.path.join(DATA_PATH, filename)
    if os.path.exists(fp):
        return send_from_directory(DATA_PATH, filename, as_attachment=True)
    return jsonify({"status": "error", "message": f"File '{filename}' not found"}), 404

@app.route("/dataflow/data/list")
@require_api_key
def list_data_files():
    files = sorted([f for f in os.listdir(DATA_PATH)])
    return jsonify({"status": "success", "files": files})

# ------------------ ARCHIVE ROUTES ------------------ #
@app.route("/dataflow/archive", methods=["GET", "POST"])
@require_api_key
def manage_archives():
    if request.method == "POST":
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"archive_{ts}.zip"
        archive_path = os.path.join(ARCHIVE_PATH, archive_name)
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for f in os.listdir(DATA_PATH): zipf.write(os.path.join(DATA_PATH, f), f)
        return jsonify({"status": "success", "archive": archive_name})
    return jsonify({"status": "success", "archives": sorted(os.listdir(ARCHIVE_PATH))})

@app.route("/dataflow/archive/<path:filename>")
@require_api_key
def get_archive(filename):
    fp = os.path.join(ARCHIVE_PATH, filename)
    if os.path.exists(fp): return send_from_directory(ARCHIVE_PATH, filename, as_attachment=True)
    return jsonify({"status": "error", "message": f"Archive '{filename}' not found"}), 404

# ------------------ VOXIA MANIFEST ------------------ #
@app.route("/voxia/manifest")
@require_api_key
def voxia_manifest():
    manifest_path = "/srv/vault_of_memories_git/system/voxia_pkw_studio_assistant/voxia_manifest.yaml"
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = yaml.safe_load(f)
        pkg_root = manifest.get("voxia_manifest", {}).get("package", {}).get("root_path")
        settings = manifest.get("voxia_manifest", {}).get("settings", {})
        def read_md(p): 
            fp = os.path.join(pkg_root, p)
            return open(fp, "r", encoding="utf-8").read() if os.path.exists(fp) else f"# Missing: {p}"
        return jsonify({
            "status": "success",
            "kind": "voxia_package",
            "manifest": manifest,
            "tone": read_md(settings.get("default_tone", "")),
            "behaviour": read_md(settings.get("default_behaviour", "")),
            "overrides": [read_md(p) for p in settings.get("override_files", [])]
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ------------------ OPENAPI SERVE ROUTE ------------------ #
@app.route("/openapi.json")
def serve_openapi():
    return send_from_directory(os.path.dirname(__file__), "openapi.json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
