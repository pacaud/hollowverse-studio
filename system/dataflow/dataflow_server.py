from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import zipfile
from datetime import datetime
from functools import wraps

app = Flask(__name__)
CORS(app, resources={r"/dataflow/*": {"origins": "*"}, r"/ping": {"origins": "*"}})

# === API Key Security ===
API_KEY = os.environ.get("VOXIA_DATAFLOW_TOKEN", "s0meSuperL0ngRandomString123!")

def require_api_key(func):
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

# === Routes ===
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Voxia Dataflow Server is running (secured)",
        "routes": {
            "PING": "/ping",
            "POST": "/dataflow/post",
            "GET": "/dataflow/get/<filename>",
            "ARCHIVE": "/dataflow/archive"
        }
    }), 200

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "source": "voxia-dataflow"}), 200

@app.route("/dataflow/post", methods=["POST"])
@require_api_key
def post_data():
    if 'file' in request.files:
        file = request.files['file']
        save_path = os.path.join(INCOMING_PATH, file.filename)
        file.save(save_path)
        return jsonify({"status": "success", "message": f"File {file.filename} saved to incoming/."}), 200
    elif request.json:
        data = request.json
        filename = data.get('filename', f"data_{datetime.now().strftime('%Y%m%d_%H%M%S")}.json")
        filepath = os.path.join(INCOMING_PATH, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(data))
        return jsonify({"status": "success", "message": f"JSON data saved as {filename}."}), 200
    return jsonify({"status": "error", "message": "No data received."}), 400

@app.route("/dataflow/get/<path:filename>", methods=["GET"])
@require_api_key
def get_data(filename):
    file_path = os.path.join(OUTGOING_PATH, filename)
    if os.path.exists(file_path):
        return send_from_directory(OUTGOING_PATH, filename, as_attachment=True)
    return jsonify({"status": "error", "message": f"File {filename} not found in outgoing/."}), 404

@app.route("/dataflow/archive", methods=["POST"])
@require_api_key
def archive_data():
    archive_name = f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S")}.zip"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
