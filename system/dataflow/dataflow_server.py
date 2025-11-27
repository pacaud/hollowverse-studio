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
API_KEY = os.environ.get("VOXIA_DATAFLOW_TOKEN", "uG2j48nRz7!mA@pF9xQvT1yCwK5oS")

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
DATA_PATH = os.path.join(FOLDER_PATH, "data")
ARCHIVE_PATH = os.path.join(FOLDER_PATH, "archives")
<<<<<<< HEAD

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(ARCHIVE_PATH, exist_ok=True)
=======
>>>>>>> 34ecdeed4b1153d6f4f9d89c675fd07ad1f677d0

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(ARCHIVE_PATH, exist_ok=True)

# === Routes ===

@app.route("/", methods=["GET"])
def home():
    """Health endpoint listing available routes."""
    return jsonify({
        "message": "Voxia Dataflow Server is running (secured, single-folder mode)",
        "routes": {
            "ping": "/ping",
            "post": "/dataflow/post",
<<<<<<< HEAD
            "get": "/dataflow/get/<filename>"
=======
            "get": "/dataflow/get/<filename>",
            "archives": "/dataflow/archive"
>>>>>>> 34ecdeed4b1153d6f4f9d89c675fd07ad1f677d0
        }
    }), 200


@app.route("/ping", methods=["GET"])
def ping():
    """Simple health check route."""
    return jsonify({"status": "ok", "source": "voxia-dataflow"}), 200


# === Data Upload ===
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
            "message": f"File '{filename}' saved to /data."
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
            "message": f"JSON data saved as '{filename}' in /data."
        }), 200

    logging.warning(f"No data received from {request.remote_addr}")
    return jsonify({"status": "error", "message": "No data received."}), 400


# === Data Retrieval ===
@app.route("/dataflow/get/<path:filename>", methods=["GET"])
@require_api_key
def get_data(filename):
    """Retrieve a file from /data."""
    filename = secure_filename(filename)
    file_path = os.path.join(DATA_PATH, filename)
    if os.path.exists(file_path):
        logging.info(f"File served: {filename} to {request.remote_addr}")
        return send_from_directory(DATA_PATH, filename, as_attachment=True)
<<<<<<< HEAD
=======

>>>>>>> 34ecdeed4b1153d6f4f9d89c675fd07ad1f677d0
    logging.warning(f"Requested file not found: {filename}")
    return jsonify({
        "status": "error",
        "message": f"File '{filename}' not found in /data."
    }), 404


<<<<<<< HEAD
# === (Placeholder) Archives ===
@app.route("/dataflow/archive", methods=["GET"])
@require_api_key
def list_archives():
    """List available archives (future use)."""
    archives = sorted(os.listdir(ARCHIVE_PATH))
=======
# === Archives ===
@app.route("/dataflow/archive", methods=["GET", "POST"])
@require_api_key
def list_or_create_archives():
    """
    GET: List all available archives in /archives.
    POST: Create a ZIP archive of all files in /data.
    """
    os.makedirs(ARCHIVE_PATH, exist_ok=True)

    if request.method == "POST":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archive_name = f"archive_{timestamp}.zip"
        archive_fullpath = os.path.join(ARCHIVE_PATH, archive_name)

        # Create zip from current /data folder
        with zipfile.ZipFile(archive_fullpath, "w", zipfile.ZIP_DEFLATED) as zipf:
            for filename in os.listdir(DATA_PATH):
                filepath = os.path.join(DATA_PATH, filename)
                if os.path.isfile(filepath):
                    zipf.write(filepath, filename)

        logging.info(f"Created new archive: {archive_name}")
        return jsonify({
            "status": "success",
            "message": f"Archive '{archive_name}' created successfully.",
            "archive": archive_name
        }), 201

    # Handle GET (list)
    archives = sorted(os.listdir(ARCHIVE_PATH))
    if not archives:
        logging.info(f"No archives found in {ARCHIVE_PATH}")
        return jsonify({
            "status": "success",
            "archives": [],
            "message": "No archives currently available."
        }), 200

>>>>>>> 34ecdeed4b1153d6f4f9d89c675fd07ad1f677d0
    logging.info(f"Listed {len(archives)} archives for {request.remote_addr}")
    return jsonify({
        "status": "success",
        "archives": archives
    }), 200


@app.route("/dataflow/archive/<path:filename>", methods=["GET"])
@require_api_key
def get_archive(filename):
    """Download a specific archive."""
    filename = secure_filename(filename)
    file_path = os.path.join(ARCHIVE_PATH, filename)

    if os.path.exists(file_path):
        logging.info(f"Archive served: {filename} to {request.remote_addr}")
        return send_from_directory(ARCHIVE_PATH, filename, as_attachment=True)

    logging.warning(f"Archive not found: {filename}")
    return jsonify({
        "status": "error",
        "message": f"Archive '{filename}' not found."
    }), 404


# === Entry Point ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)

