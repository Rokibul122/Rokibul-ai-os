from flask_cors import CORS

cors = CORS()

সপ্তম ফাইল: app/init.py

from flask import Flask, jsonify, render_template

from app.config import Config
from app.extensions import cors

def create_app(config_class=Config):
app = Flask(
name,
template_folder="templates",
static_folder="static"
)

app.config.from_object(config_class)

cors.init_app(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5000",
                "http://127.0.0.1:5000"
            ]
        }
    }
)

from app.api.routes.system import system_bp
from app.api.routes.projects import projects_bp
from app.api.routes.memory import memory_bp
from app.api.routes.tasks import tasks_bp

app.register_blueprint(system_bp, url_prefix="/api/system")
app.register_blueprint(projects_bp, url_prefix="/api/projects")
app.register_blueprint(memory_bp, url_prefix="/api/memory")
app.register_blueprint(tasks_bp, url_prefix="/api/tasks")

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/health")
def health():
    return jsonify({
        "success": True,
        "application": app.config["APP_NAME"],
        "version": app.config["APP_VERSION"],
        "status": "running"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Resource not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

return app
