"""
TaskForge Lite - Flask API Application
Pure Python backend service untuk mengelola task (to-do) tanpa database.
"""

from flask import Flask

from handlers.task_handler import task_bp
from handlers.user_handler import user_bp


def create_app() -> Flask:
    """
    Factory function untuk membuat Flask application instance.

    Returns:
        Flask: Application instance
    """
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(task_bp)

    @app.route("/health", methods=["GET"])
    def health_check():
        return {"status": "healthy"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
