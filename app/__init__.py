from flask import Flask, jsonify

from app.config import Config
from app.extensions import cors
from app.database import init_db, close_db


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    cors.init_app(app)

    # Close database connection after each request
    app.teardown_appcontext(close_db)

    # Initialize database tables
    with app.app_context():
        init_db()

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
            "status": "running",
            "application": app.config["APP_NAME"],
            "database": "initialized"
        })

    return app
