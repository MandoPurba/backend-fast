"""
Task Service Layer
Berisi business logic untuk akses data task.
"""

from database import inmemory


class TaskService:
    """Service untuk operasi CRUD pada task"""

    def __init__(self, db=inmemory):
        self.db = db

    def create_task(self, user_id: int, title: str) -> dict:
        """Buat task baru untuk user tertentu"""
        # TODO: Validasi user_id & title, cek duplicate + limit, panggil db.create_task
        pass

    def get_all_tasks(self) -> list[dict]:
        """Ambil semua task"""
        # TODO: Ambil semua via db.get_all_tasks
        pass

    def get_tasks_by_user(self, user_id: int) -> list[dict]:
        """Ambil semua task berdasarkan user_id"""
        # TODO: Ambil semua via db.get_tasks_by_user
        pass

    def get_task_by_id(self, task_id: int) -> dict:
        """Ambil task berdasarkan id"""
        # TODO: Ambil task via db.get_task_by_id, raise ValueError jika None
        pass

    def mark_task_completed(self, task_id: int) -> dict:
        """Tandai task sebagai completed"""
        # TODO: Pastikan task ada, lalu update is_completed via db.update_task
        pass

    def delete_task(self, task_id: int) -> bool:
        """Hapus task berdasarkan id"""
        # TODO: Pastikan task ada, lalu hapus via db.delete_task
        pass


# Singleton instance
task_service = TaskService()
