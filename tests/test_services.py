"""Unit Tests untuk Service Layer"""

import pytest

from database.inmemory import reset_data
from services.task_service import TaskService
from services.user_service import UserService


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Reset data sebelum setiap test"""
    reset_data()
    yield
    reset_data()


@pytest.fixture
def user_service():
    """Fixture untuk UserService"""
    return UserService()


@pytest.fixture
def task_service():
    """Fixture untuk TaskService"""
    return TaskService()


class TestUserService:
    """Test untuk UserService"""

    def test_create_user_success(self, user_service):
        """create_user berhasil membuat user baru"""
        user = user_service.create_user("Charlie")
        assert "id" in user, "Expected created user to include an 'id' field"
        assert user["name"] == "Charlie", "Expected created user name to be 'Charlie'"

    def test_create_user_empty_name(self, user_service):
        """create_user gagal jika name kosong"""
        with pytest.raises(ValueError):
            user_service.create_user("")

    def test_get_user_by_id_found(self, user_service):
        """get_user_by_id mengembalikan user jika ada"""
        user = user_service.get_user_by_id(1)
        assert user["id"] == 1, "Expected user id to be 1"
        assert user["name"] == "Alice", "Expected user name to be 'Alice'"

    def test_get_user_by_id_not_found(self, user_service):
        """get_user_by_id raise ValueError jika user tidak ada"""
        with pytest.raises(ValueError):
            user_service.get_user_by_id(999)

    def test_get_all_users(self, user_service):
        """get_all_users mengembalikan semua user"""
        users = user_service.get_all_users()
        assert isinstance(users, list), "Expected get_all_users() to return a list"
        assert len(users) == 2, f"Expected 2 users, got {len(users)}"


class TestTaskService:
    """Test untuk TaskService"""

    def test_create_task_success(self, task_service):
        """create_task berhasil membuat task baru"""
        task = task_service.create_task(user_id=1, title="New task")
        assert "id" in task, "Expected created task to include an 'id' field"
        assert task["title"] == "New task", "Expected task title to be 'New task'"
        assert task["user_id"] == 1, "Expected task user_id to be 1"
        assert task["is_completed"] is False, "Expected is_completed to default False"

    def test_create_task_user_not_found(self, task_service):
        """create_task gagal jika user tidak ada"""
        with pytest.raises(ValueError):
            task_service.create_task(user_id=999, title="Missing user task")

    def test_create_task_empty_title(self, task_service):
        """create_task gagal jika title kosong"""
        with pytest.raises(ValueError):
            task_service.create_task(user_id=1, title="")

    def test_create_task_duplicate_title(self, task_service):
        """create_task gagal jika title duplicate untuk user sama"""
        task_service.create_task(user_id=1, title="Buy groceries")
        with pytest.raises(ValueError):
            task_service.create_task(user_id=1, title="Buy groceries")

    def test_create_task_max_10_per_user(self, task_service):
        """create_task gagal jika task > 10 per user"""
        for i in range(10):
            task_service.create_task(user_id=1, title=f"Task {i + 1}")
        with pytest.raises(ValueError):
            task_service.create_task(user_id=1, title="Extra task")

    def test_get_all_tasks(self, task_service):
        """get_all_tasks mengembalikan semua task"""
        tasks = task_service.get_all_tasks()
        assert isinstance(tasks, list), "Expected get_all_tasks() to return a list"
        assert len(tasks) == 3, f"Expected 3 tasks, got {len(tasks)}"

    def test_get_tasks_by_user(self, task_service):
        """get_tasks_by_user mengembalikan task sesuai user_id"""
        tasks = task_service.get_tasks_by_user(1)
        assert len(tasks) == 2, f"Expected 2 tasks for user_id=1, got {len(tasks)}"
        for task in tasks:
            assert task["user_id"] == 1, "Expected task.user_id to match user_id"

    def test_get_task_by_id_found(self, task_service):
        """get_task_by_id mengembalikan task jika ada"""
        task = task_service.get_task_by_id(1)
        assert task["id"] == 1, "Expected task id to be 1"
        assert task["title"] == "Buy groceries", (
            "Expected task title to be 'Buy groceries'"
        )

    def test_get_task_by_id_not_found(self, task_service):
        """get_task_by_id raise ValueError jika task tidak ada"""
        with pytest.raises(ValueError):
            task_service.get_task_by_id(999)

    def test_mark_task_completed_success(self, task_service):
        """mark_task_completed menandai task selesai"""
        task = task_service.mark_task_completed(1)
        assert task["is_completed"] is True, "Expected is_completed to be True"

    def test_mark_task_completed_not_found(self, task_service):
        """mark_task_completed raise ValueError jika task tidak ada"""
        with pytest.raises(ValueError):
            task_service.mark_task_completed(999)

    def test_delete_task_success(self, task_service):
        """delete_task menghapus task jika ada"""
        result = task_service.delete_task(1)
        assert result is True, "Expected delete_task to return True"

    def test_delete_task_not_found(self, task_service):
        """delete_task raise ValueError jika task tidak ada"""
        with pytest.raises(ValueError):
            task_service.delete_task(999)
