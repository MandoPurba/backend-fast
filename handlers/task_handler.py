"""
Task Handler Layer - Flask API endpoints for TaskForge Lite
Mendefinisikan endpoint-endpoint API untuk operasi task.
"""

from dataclasses import dataclass

from flask import Blueprint, jsonify, request


@dataclass
class CreateTaskRequest:
    """Request body untuk membuat task baru"""

    user_id: int
    title: str


# Flask Blueprint untuk task endpoints
task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@task_bp.route("", methods=["POST"])
def create_task_handler():
    """
    Handler untuk endpoint create task.

    POST /tasks
    Body: {"user_id": int, "title": str}
    """
    # TODO: Validasi body (user_id/title), panggil service, handle error/limit/duplicate
    pass


@task_bp.route("", methods=["GET"])
def get_all_tasks_handler():
    """
    Handler untuk endpoint get all tasks.

    GET /tasks
    """
    # TODO: Ambil semua task via service, return JSON
    pass


@task_bp.route("/<int:task_id>", methods=["GET"])
def get_task_by_id_handler(task_id: int):
    """
    Handler untuk endpoint get task by ID.

    GET /tasks/<task_id>
    """
    # TODO: Ambil task by id via service, handle not found (404)
    pass


@task_bp.route("/user/<int:user_id>", methods=["GET"])
def get_tasks_by_user_handler(user_id: int):
    """
    Handler untuk endpoint get tasks by user.

    GET /tasks/user/<user_id>
    """
    # TODO: Ambil task by user_id via service, return JSON
    pass


@task_bp.route("/<int:task_id>/complete", methods=["PATCH"])
def mark_task_completed_handler(task_id: int):
    """
    Handler untuk endpoint mark task as completed.

    PATCH /tasks/<task_id>/complete
    """
    # TODO: Implementasi
    pass


@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task_handler(task_id: int):
    """
    Handler untuk endpoint delete task.

    DELETE /tasks/<task_id>
    """
    # TODO: Implementasi
    pass
