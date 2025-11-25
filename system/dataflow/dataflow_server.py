from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import zipfile
import logging
from datetime import datetime
from functools import wraps

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
API_KEY = os.environ.get("VOXIA_DATAFLOW_TOKEN", "s0meSuperL0ngRandomString123!")

def require_api_key(func):
    """Decorator to enforce API key authentication."""
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
DATA_PATH = os.path.join(FOLDER_PATH, "data")      # ✅ unified folder for get/post
ARCHIVE_PATH = os.path.join(FOLDER_PATH, "archive")

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(ARCHIVE_PATH, exist_ok=True)


# === Routes ===

@app.route("/", methods=["GET"])
def home():
    """Health endpoint listing available routes."""
    return jsonify({
        "message": "Voxia Dataflow Server is running (secured)",
        "routes": {
            "ping": "/ping",
            "post": "/dataflow/post",
            "get": "/dataflow/get/<filename>",
            "archive": "/dataflow/archive"
        }
    }), 200


@app.route("/ping", methods=["GET"])
def ping():
    """Basic heartbeat endpoint."""
    return jsonify({"status": "ok", "source": "voxia-dataflow"}), 200


# === Upload Endpoint (POST) ===
@app.route("/dataflow/post", methods=["POST"])
@require_api_key
def post_data():
    """Accept a file or JSON payload and save it to /data."""
    if "file" in request.files:
        file = request.files["file"]
        filename = secure_filename(file.filename)
        save_path = os.path.join(DATA_PATH, filename)
        file.save(save_path)

        logging.info(f"Uploaded file: {filename} from {request.remote_addr}")
        return jsonify({
            "status": "success",
            "message": f"File '{filename}' saved to data directory."
        }), 200

    elif request.is_json:
        data = request.get_json()
        filename = data.get("filename", f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        filepath = os.path.join(DATA_PATH, secure_filename(filename))
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(data))

        logging.info(f"Received JSON payload as '{filename}' from {request.remote_addr}")
        return jsonify({
            "status": "success",
            "message": f"JSON data saved as '{filename}' in data directory."
        }), 200

    logging.warning(f"No data received from {request.remote_addr}")
    return jsonify({"status": "error", "message": "No data received."}), 400


# === Download Endpoint (GET) ===
@app.route("/dataflow/get/<path:filename>", methods=["GET"])
@require_api_key
def get_data(filename):
    """Retrieve a file from /data."""
    filename = secure_filename(filename)
    file_path = os.path.join(DATA_PATH, filename)
    if os.path.exists(file_path):
        logging.info(f"File served: {filename} to {request.remote_addr}")
        return send_from_directory(DATA_PATH, filename, as_attachment=True)
    logging.warning(f"Requested file not found: {filename}")
    return jsonify({
        "status": "error",
        "message": f"File '{filename}' not found in data directory."
    }), 404


# === Archive Management ===
@app.route("/dataflow/archive", methods=["GET", "POST"])
@require_api_key
def manage_archive():
    """
    POST: Archive all files from /data into /archive.
    GET: List available archives.
    """
    if request.method == "POST":
        archive_name = f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        archive_path = os.path.join(ARCHIVE_PATH, archive_name)

        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive_zip:
            for root, _, files in os.walk(DATA_PATH):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, DATA_PATH)
                    archive_zip.write(full_path, arcname)

        # Clean up /data after archiving
        for file in os.listdir(DATA_PATH):
            os.remove(os.path.join(DATA_PATH, file))

        logging.info(f"Archived files to '{archive_name}' by {request.remote_addr}")
        return jsonify({
            "status": "success",
            "message": f"Archived data files to '{archive_name}'."
        }), 200

    # GET: list available archives
    archives = sorted(os.listdir(ARCHIVE_PATH))
    logging.info(f"Listed {len(archives)} archives for {request.remote_addr}")
    return jsonify({
        "status": "success",
        "archives": archives
    }), 200


# === Entry Point ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
