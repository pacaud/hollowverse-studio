from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import zipfile
import logging
from datetime import datetime
from functools import wraps
import yaml

# === Flask App Setup ===
app = Flask(__name__)
CORS(app, resources={
    r"/dataflow/*": {"origins": "*"},
    r"/ping": {"origins": "*"}
})

# === Logging Configuration ===
LOG_DIR = "/var/log/voxia"
LOG_FILE = os.path.join(LOG_DIR, "dataflow.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# === API Key Security ===
API_KEY = os.environ.get("VOXIA_DATAFLOW_TOKEN", "uG2j48nRz7!mA@pF9xQvT1yCwK5oS")

def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if key != API_KEY:
            logging.warning(f"Unauthorized access attempt from {request.remote_addr}")
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper

# === Directory Setup ===
FOLDER_PATH = "/var/www/dataflow.hollowverse"
DATA_PATH = os.path.join(FOLDER_PATH, "data")
ARCHIVE_PATH = os.path.join(FOLDER_PATH, "archives")

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(ARCHIVE_PATH, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Voxia Dataflow Server is running (secured, single-folder mode)",
        "routes": {
            "ping": "/ping",
            "post": "/dataflow/post",
            "get": "/dataflow/get/<filename>",
            "data_list": "/dataflow/data/list",
            "archives": "/dataflow/archive"
        }
    }), 200

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "source": "voxia-dataflow"}), 200

@app.route("/dataflow/post", methods=["POST"])
@require_api_key
def post_data():
    if "file" in request.files:
        file = request.files["file"]
        filename = secure_filename(file.filename)
        save_path = os.path.join(DATA_PATH, filename)
        file.save(save_path)
        logging.info(f"Uploaded file: {filename} from {request.remote_addr}")
        return jsonify({"status": "success", "message": f"File '{filename}' saved to /data."}), 200
    elif request.is_json:
        data = request.get_json()
        filename = data.get("filename", f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        filepath = os.path.join(DATA_PATH, secure_filename(filename))
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(data))
        logging.info(f"Received JSON payload as '{filename}' from {request.remote_addr}")
        return jsonify({"status": "success", "message": f"JSON data saved as '{filename}' in /data."}), 200
    logging.warning(f"No data received from {request.remote_addr}")
    return jsonify({"status": "error", "message": "No data received."}), 400

@app.route("/dataflow/get/<path:filename>", methods=["GET"])
@require_api_key
def get_data(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(DATA_PATH, filename)
    if os.path.exists(file_path):
        logging.info(f"File served: {filename} to {request.remote_addr}")
        return send_from_directory(DATA_PATH, filename, as_attachment=True)
    logging.warning(f"Requested file not found: {filename}")
    return jsonify({"status": "error", "message": f"File '{filename}' not found in /data."}), 404

@app.route("/dataflow/data/list", methods=["GET"])
@require_api_key
def list_data_files():
    files = []
    for root, dirs, filenames in os.walk(DATA_PATH):
        for name in filenames:
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, DATA_PATH).replace(os.sep, "/")
            files.append(rel_path)
    files.sort()
    logging.info(f"Listed {len(files)} data files for {request.remote_addr}")
    return jsonify({"status": "success", "files": files}), 200

@app.route("/dataflow/archive", methods=["GET", "POST"])
@require_api_key
def list_or_create_archives():
    os.makedirs(ARCHIVE_PATH, exist_ok=True)
    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"archive_{timestamp}.zip"
        archive_fullpath = os.path.join(ARCHIVE_PATH, archive_name)
        with zipfile.ZipFile(archive_fullpath, "w", zipfile.ZIP_DEFLATED) as zipf:
            for filename in os.listdir(DATA_PATH):
                filepath = os.path.join(DATA_PATH, filename)
                if os.path.isfile(filepath):
                    zipf.write(filepath, filename)
        logging.info(f"Created new archive: {archive_name}")
        return jsonify({"status": "success", "message": f"Archive '{archive_name}' created successfully.", "archive": archive_name}), 201
    archives = sorted(os.listdir(ARCHIVE_PATH))
    return jsonify({"status": "success", "archives": archives, "message": "Archives listed."}), 200

@app.route("/dataflow/archive/<path:filename>", methods=["GET"])
@require_api_key
def get_archive(filename):
    filename = secure_filename(filename)
    file_path = os.path.join(ARCHIVE_PATH, filename)
    if os.path.exists(file_path):
        logging.info(f"Archive served: {filename} to {request.remote_addr}")
        return send_from_directory(ARCHIVE_PATH, filename, as_attachment=True)
    logging.warning(f"Archive not found: {filename}")
    return jsonify({"status": "error", "message": f"Archive '{filename}' not found."}), 404

# === Voxia Manifest Recursive Loader ===
@app.route("/voxia/manifest", methods=["GET"])
@require_api_key
def voxia_manifest():
    manifest_path = "/srv/vault_of_memories_git/system/voxia_pkw_studio_assistant/voxia_manifest.yaml"
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = yaml.safe_load(f)
        pkg_root = manifest.get("voxia_manifest", {}).get("package", {}).get("root_path")
        settings = manifest.get("voxia_manifest", {}).get("settings", {})
        if not pkg_root or not os.path.isdir(pkg_root):
            return jsonify({"status": "error", "message": f"Voxia package root path not found: {pkg_root}"}), 500

        def safe_read(rel_path):
            abs_path = os.path.join(pkg_root, rel_path)
            if os.path.exists(abs_path):
                with open(abs_path, "r", encoding="utf-8") as f:
                    return f.read()
            return f"# Missing: {rel_path}"

        tone = safe_read(settings.get("default_tone", ""))
        behaviour = safe_read(settings.get("default_behaviour", ""))
        overrides = [safe_read(p) for p in settings.get("override_files", [])]

        return jsonify({
            "status": "success",
            "kind": "voxia_package",
            "manifest": manifest,
            "tone": tone,
            "behaviour": behaviour,
            "overrides": overrides
        }), 200

    except Exception as e:
        logging.exception("Error loading Voxia package")
        return jsonify({"status": "error", "message": f"Failed to load Voxia package: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
