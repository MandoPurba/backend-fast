"""Unit Tests untuk Handler Layer (Flask API)"""

import pytest
from flask import Flask

from database.inmemory import reset_data


@pytest.fixture
def app():
    """Fixture untuk membuat Flask app"""
    from app import create_app
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client(app):
    """Fixture untuk test client"""
    return app.test_client()


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Reset data sebelum setiap test"""
    reset_data()
    yield
    reset_data()


class TestHealthCheck:
    """Test untuk health check endpoint"""

    def test_health_check_returns_healthy(self, client):
        """GET /health mengembalikan status healthy"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"


class TestUserHandler:
    """Test untuk User Handler API"""

    def test_create_user_success(self, client):
        """POST /users - berhasil membuat user baru"""
        response = client.post("/users", json={"name": "Charlie"})
        assert response.status_code == 201
        data = response.get_json()
        assert data["name"] == "Charlie"
        assert "id" in data

    def test_create_user_missing_name(self, client):
        """POST /users - gagal jika name kosong"""
        response = client.post("/users", json={"name": ""})
        assert response.status_code == 400

    def test_list_users(self, client):
        """GET /users - mendapatkan semua user"""
        response = client.get("/users")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 2
        assert data[0]["name"] == "Alice"
        assert data[1]["name"] == "Bob"

    def test_get_user_by_id_found(self, client):
        """GET /users/<user_id> - user ditemukan"""
        response = client.get("/users/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["name"] == "Alice"

    def test_get_user_by_id_not_found(self, client):
        """GET /users/<user_id> - user tidak ditemukan"""
        response = client.get("/users/99")
        assert response.status_code == 404


class TestTaskHandler:
    """Test untuk Task Handler API"""

    def test_create_task_success(self, client):
        """POST /tasks - berhasil membuat task baru"""
        response = client.post("/tasks", json={
            "user_id": 1,
            "title": "New task"
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "New task"
        assert data["user_id"] == 1
        assert data["is_completed"] is False

    def test_create_task_user_not_found(self, client):
        """POST /tasks - gagal jika user tidak ada"""
        response = client.post("/tasks", json={
            "user_id": 99,
            "title": "Some task"
        })
        assert response.status_code == 404

    def test_create_task_empty_title(self, client):
        """POST /tasks - gagal jika title kosong"""
        response = client.post("/tasks", json={
            "user_id": 1,
            "title": ""
        })
        assert response.status_code == 400

    def test_create_task_duplicate_title(self, client):
        """POST /tasks - gagal jika title duplicate untuk user sama"""
        client.post("/tasks", json={"user_id": 1, "title": "Buy groceries"})
        response = client.post("/tasks", json={
            "user_id": 1,
            "title": "Buy groceries"
        })
        assert response.status_code == 409

    def test_create_task_max_10_per_user(self, client):
        """POST /tasks - maksimal 10 task per user"""
        for i in range(10):
            client.post("/tasks", json={
                "user_id": 1,
                "title": f"Task {i + 1}"
            })
        response = client.post("/tasks", json={
            "user_id": 1,
            "title": "Extra task"
        })
        assert response.status_code == 400

    def test_get_all_tasks(self, client):
        """GET /tasks - mendapatkan semua task"""
        response = client.get("/tasks")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 3

    def test_get_task_by_id_found(self, client):
        """GET /tasks/<task_id> - task ditemukan"""
        response = client.get("/tasks/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["title"] == "Buy groceries"

    def test_get_task_by_id_not_found(self, client):
        """GET /tasks/<task_id> - task tidak ditemukan"""
        response = client.get("/tasks/99")
        assert response.status_code == 404

    def test_get_tasks_by_user(self, client):
        """GET /tasks/user/<user_id> - mendapatkan task berdasarkan user"""
        response = client.get("/tasks/user/1")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 2
        for task in data:
            assert task["user_id"] == 1

    def test_mark_task_completed_success(self, client):
        """PATCH /tasks/<task_id>/complete - menandai task selesai"""
        response = client.patch("/tasks/1/complete")
        assert response.status_code == 200
        data = response.get_json()
        assert data["is_completed"] is True

    def test_mark_task_completed_not_found(self, client):
        """PATCH /tasks/<task_id>/complete - task tidak ditemukan"""
        response = client.patch("/tasks/99/complete")
        assert response.status_code == 404

    def test_delete_task_success(self, client):
        """DELETE /tasks/<task_id> - berhasil menghapus task"""
        response = client.delete("/tasks/1")
        assert response.status_code == 200
        data = response.get_json()
        assert data["message"] == "Task deleted successfully"

    def test_delete_task_not_found(self, client):
        """DELETE /tasks/<task_id> - task tidak ditemukan"""
        response = client.delete("/tasks/99")
        assert response.status_code == 404

    def test_delete_task_leaves_other_tasks(self, client):
        """DELETE /tasks/<task_id> - menghapus task tidak affect task lain"""
        client.delete("/tasks/1")
        response = client.get("/tasks")
        data = response.get_json()
        assert len(data) == 2


class TestEdgeCases:
    """Test untuk edge cases"""

    def test_same_title_different_users(self, client):
        """Title sama boleh dipakai user berbeda"""
        client.post("/tasks", json={"user_id": 1, "title": "Buy groceries"})
        response = client.post("/tasks", json={"user_id": 2, "title": "Buy groceries"})
        assert response.status_code == 201

    def test_task_title_case_sensitive(self, client):
        """Title Buy Groceries dan buy groceries dianggap berbeda"""
        client.post("/tasks", json={"user_id": 1, "title": "Buy Groceries"})
        response = client.post("/tasks", json={"user_id": 1, "title": "buy groceries"})
        assert response.status_code == 201
