from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import zipfile
from datetime import datetime
from functools import wraps

# === Initialize Flask ===
app = Flask(__name__)
CORS(app, resources={
    r"/dataflow/*": {"origins": "*"},
    r"/ping": {"origins": "*"},
    r"/api/*": {"origins": "*"}
})

# === Security (API Key) ===
API_KEY = os.environ.get("VOXIA_DATAFLOW_TOKEN", "s0meSuperL0ngRandomString123!")

def require_api_key(func):
    """Decorator to require the X-API-Key header for access."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper

# === Directory Setup ===
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INCOMING_PATH = os.path.join(BASE_PATH, "incoming")
OUTGOING_PATH = os.path.join(BASE_PATH, "outgoing")
ARCHIVE_PATH = os.path.join(BASE_PATH, "archive")

for path in (INCOMING_PATH, OUTGOING_PATH, ARCHIVE_PATH):
    os.makedirs(path, exist_ok=True)

# === Root Endpoint ===
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Voxia Dataflow Server is running (secured)",
        "routes": {
            "PING": ["/ping", "/api/ping"],
            "POST": "/dataflow/post",
            "GET": "/dataflow/get/<filename>",
            "ARCHIVE": "/dataflow/archive"
        }
    }), 200

# === API Root Endpoint ===
@app.route("/api", methods=["GET"])
def api_root():
    """Returns API index overview."""
    return jsonify({
        "message": "Voxia Dataflow API root endpoint",
        "status": "available",
        "routes": {
            "ping": "/api/ping",
            "post": "/dataflow/post",
            "get": "/dataflow/get/<filename>",
            "archive": "/dataflow/archive"
        }
    }), 200

# === Health Check Routes ===
@app.route("/ping", methods=["GET"])
@app.route("/api/ping", methods=["GET"])
def ping():
    """Simple health check route."""
    return jsonify({"status": "ok", "source": "voxia-dataflow"}), 200

# === POST: Upload or Send JSON ===
@app.route("/dataflow/post", methods=["POST"])
@require_api_key
def post_data():
    """Accepts a file or JSON payload and stores it in the incoming directory."""
    if 'file' in request.files:
        file = request.files['file']
        save_path = os.path.join(INCOMING_PATH, file.filename)
        file.save(save_path)
        return jsonify({"status": "success", "message": f"File {file.filename} saved to incoming/."}), 200

    elif request.json:
        data = request.json
        filename = data.get('filename', f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        filepath = os.path.join(INCOMING_PATH, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(data))
        return jsonify({"status": "success", "message": f"JSON data saved as {filename}."}), 200

    return jsonify({"status": "error", "message": "No data received."}), 400

# === GET: Download from outgoing ===
@app.route("/dataflow/get/<path:filename>", methods=["GET"])
@require_api_key
def get_data(filename):
    """Serves a file from the outgoing directory."""
    file_path = os.path.join(OUTGOING_PATH, filename)
    if os.path.exists(file_path):
        return send_from_directory(OUTGOING_PATH, filename, as_attachment=True)
    return jsonify({"status": "error", "message": f"File {filename} not found in outgoing/."}), 404

# === ARCHIVE: Zip all incoming files ===
@app.route("/dataflow/archive", methods=["POST"])
@require_api_key
def archive_data():
    """Zips all incoming files and moves them to the archive directory."""
    archive_name = f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    archive_path = os.path.join(ARCHIVE_PATH, archive_name)

    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive_zip:
        for root, _, files in os.walk(INCOMING_PATH):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, INCOMING_PATH)
                archive_zip.write(full_path, arcname)

    for file in os.listdir(INCOMING_PATH):
        os.remove(os.path.join(INCOMING_PATH, file))

    return jsonify({"status": "success", "message": f"Archived incoming files to {archive_name}."}), 200

# === Main Entry Point ===
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
