from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Jenkins + GCP CI/CD pipeline!",
        "environment": os.getenv("APP_ENV", "production"),
        "version": os.getenv("BUILD_NUMBER", "1")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
