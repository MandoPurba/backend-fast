"""
User Handler Layer - Flask API Endpoints for User Operations
Bertanggung jawab untuk menangani request/response API terkait user.
"""

from flask import Blueprint, jsonify, request

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("", methods=["POST"])
def create_user():
    """
    Create a new user.

    POST /users
    Body: {"name": "string"}
    """
    # TODO: Validasi body (name), panggil service, return JSON + status
    pass


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    """
    Get user by ID.

    GET /users/<user_id>
    """
    # TODO: Ambil user via service, handle not found (404)
    pass


@user_bp.route("", methods=["GET"])
def list_users():
    """
    List all users.

    GET /users
    """
    # TODO: Ambil semua user via service, return JSON
    pass
