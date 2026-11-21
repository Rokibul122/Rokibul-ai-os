from flask import Flask, jsonify
from app.config import Config
from app.extensions import cors


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)

    @app.get("/")
    def home():
        return jsonify({
            "name": app.config["APP_NAME"],
            "version": app.config["APP_VERSION"],
            "message": "ROKIBUL AI OS Backend is running"
        })

    @app.get("/api/health")
    def health():
        return jsonify({
            "success": True,
            "status": "running"
        })

    return app
