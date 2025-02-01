from flask import Flask, jsonify, send_from_directory
from routes import api_bp  # Import the Blueprint

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

# Serve static files from the frontend folder
@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('frontend', path)

# Run the Flask app
if __name__ == '__main__':
    import pyfiglet
    ascii_banner = pyfiglet.figlet_format("NBA Data API")
    print("\n" + ascii_banner)
    print("🔥 Welcome to the NBA Data API! 🔥")
    print("🚀 Server running at: http://127.0.0.1:5000/api/")
    print("===================================\n")
    
    app.run(debug=True)

