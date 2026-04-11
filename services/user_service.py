"""
User Service Layer
Berisi business logic untuk operasi user.
"""

from database import inmemory


class UserService:
    """Service untuk operasi user"""

    def __init__(self, db=inmemory):
        self.db = db

    def create_user(self, name: str) -> dict:
        """Buat user baru"""
        # TODO: Validasi name tidak kosong, panggil db.create_user
        pass

    def get_user_by_id(self, user_id: int) -> dict | None:
        """Ambil user berdasarkan id"""
        # TODO: Ambil via db.get_user_by_id, raise ValueError jika None
        pass

    def get_all_users(self) -> list[dict]:
        """Ambil semua user"""
        # TODO: Ambil semua via db.get_all_users
        pass
