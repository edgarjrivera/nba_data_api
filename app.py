from flask import Flask, jsonify, send_from_directory
from routes import api_bp

app = Flask(__name__)

# Register API routes
app.register_blueprint(api_bp, url_prefix='/api')

# Serve static files
@app.route('/')
def serve_index():
    try:
        return send_from_directory('frontend', 'index.html')
    except Exception as e:
        app.logger.error(f"Error serving index.html: {e}")
        return jsonify({"error": "File not found"}), 500

@app.route('/<path:path>')
def serve_static_files(path):
    try:
        return send_from_directory('frontend', path)
    except Exception as e:
        app.logger.error(f"Error serving static file {path}: {e}")
        return jsonify({"error": "File not found"}), 500

if __name__ == '__main__':
    import pyfiglet
    ascii_banner = pyfiglet.figlet_format("NBA Data API")
    print("\n" + ascii_banner)
    print("🔥 Welcome to the NBA Data API! 🔥")
    print("🚀 Server running at: http://127.0.0.1:5000/api/")
    print("===================================\n")

    app.run(debug=True)
