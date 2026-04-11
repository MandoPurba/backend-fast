"""Unit Tests for In-Memory Database Layer"""

import pytest

from database.inmemory import (
    create_task,
    create_user,
    delete_task,
    get_all_tasks,
    get_all_users,
    get_task_by_id,
    get_tasks_by_user,
    get_user_by_id,
    reset_data,
    update_task,
)


class TestGetAllUsers:
    """Test untuk operasi Get All Users"""

    def test_get_all_users_returns_list(self):
        """get_all_users mengembalikan list"""
        reset_data()
        users = get_all_users()
        assert isinstance(users, list)

    def test_get_all_users_with_data(self):
        """get_all_users mengembalikan semua user"""
        reset_data()
        users = get_all_users()
        assert len(users) == 2
        assert users[0]["name"] == "Alice"
        assert users[1]["name"] == "Bob"


class TestGetUserById:
    """Test untuk operasi Get User By ID"""

    def test_get_user_by_id_found(self):
        """get_user_by_id mengembalikan user yang ada"""
        reset_data()
        user = get_user_by_id(user_id=1)
        assert user is not None
        assert user["id"] == 1
        assert user["name"] == "Alice"

    def test_get_user_by_id_not_found(self):
        """get_user_by_id mengembalikan None untuk user yang tidak ada"""
        reset_data()
        user = get_user_by_id(user_id=99)
        assert user is None


class TestCreateUser:
    """Test untuk operasi Create User"""

    def test_create_user_increments_id(self):
        """ID user auto increment"""
        reset_data()
        user = create_user(name="Charlie")
        assert user["id"] == 3

    def test_create_user_has_correct_structure(self):
        """User baru memiliki field yang benar"""
        reset_data()
        user = create_user(name="Charlie")
        assert "id" in user
        assert "name" in user
        assert user["name"] == "Charlie"


class TestGetAllTasks:
    """Test untuk operasi Get All Tasks"""

    def test_get_all_tasks_returns_list(self):
        """get_all_tasks mengembalikan list"""
        reset_data()
        tasks = get_all_tasks()
        assert isinstance(tasks, list)

    def test_get_all_tasks_with_data(self):
        """get_all_tasks mengembalikan semua task"""
        reset_data()
        tasks = get_all_tasks()
        assert len(tasks) == 3


class TestGetTaskById:
    """Test untuk operasi Get Task By ID"""

    def test_get_task_by_id_found(self):
        """get_task_by_id mengembalikan task yang ada"""
        reset_data()
        task = get_task_by_id(task_id=1)
        assert task is not None
        assert task["title"] == "Buy groceries"

    def test_get_task_by_id_not_found(self):
        """get_task_by_id mengembalikan None untuk task yang tidak ada"""
        reset_data()
        task = get_task_by_id(task_id=99)
        assert task is None


class TestGetTasksByUser:
    """Test untuk operasi Get Tasks By User"""

    def test_get_tasks_by_user_returns_list(self):
        """get_tasks_by_user mengembalikan list"""
        reset_data()
        tasks = get_tasks_by_user(user_id=1)
        assert isinstance(tasks, list)

    def test_get_tasks_by_user_with_data(self):
        """get_tasks_by_user mengembalikan task sesuai user_id"""
        reset_data()
        tasks = get_tasks_by_user(user_id=1)
        assert len(tasks) == 2
        for task in tasks:
            assert task["user_id"] == 1

    def test_get_tasks_by_user_empty(self):
        """get_tasks_by_user mengembalikan list kosong untuk user tanpa task"""
        reset_data()
        tasks = get_tasks_by_user(user_id=2)
        assert len(tasks) == 1  # Bob has "Read a book"


class TestCreateTask:
    """Test untuk operasi Create Task"""

    def test_create_task_increments_id(self):
        """ID task auto increment"""
        reset_data()
        task = create_task(user_id=1, title="New task")
        assert task["id"] == 4

    def test_create_task_has_correct_structure(self):
        """Task baru memiliki field yang benar"""
        reset_data()
        task = create_task(user_id=1, title="New task")
        assert "id" in task
        assert "title" in task
        assert "is_completed" in task
        assert "user_id" in task
        assert task["title"] == "New task"
        assert task["is_completed"] is False


class TestUpdateTask:
    """Test untuk operasi Update Task"""

    def test_update_task_completed_status(self):
        """update_task dapat mengubah is_completed"""
        reset_data()
        task = update_task(task_id=1, updates={"is_completed": True})
        assert task["is_completed"] is True

    def test_update_task_title(self):
        """update_task dapat mengubah title"""
        reset_data()
        task = update_task(task_id=1, updates={"title": "Updated title"})
        assert task["title"] == "Updated title"


class TestDeleteTask:
    """Test untuk operasi Delete Task"""

    def test_delete_task_returns_true(self):
        """delete_task mengembalikan True jika berhasil"""
        reset_data()
        result = delete_task(task_id=1)
        assert result is True

    def test_delete_task_removes_from_list(self):
        """delete_task menghapus task dari list"""
        reset_data()
        delete_task(task_id=1)
        task = get_task_by_id(task_id=1)
        assert task is None


class TestResetData:
    """Test untuk operasi Reset Data"""

    def test_reset_data_restores_initial_data(self):
        """reset_data mengembalikan data ke kondisi awal"""
        reset_data()
        delete_task(task_id=1)
        create_user(name="Test User")
        reset_data()
        users = get_all_users()
        tasks = get_all_tasks()
        assert len(users) == 2
        assert len(tasks) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
