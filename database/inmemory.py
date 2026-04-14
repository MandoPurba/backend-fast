"""
In-Memory Database for TaskForge Lite
Pure Python backend service untuk mengelola task (to-do) tanpa database.
"""

# In-memory data storage
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

tasks = [
    {"id": 1, "title": "Buy groceries", "is_completed": False, "user_id": 1},
    {"id": 2, "title": "Walk the dog", "is_completed": True, "user_id": 1},
    {"id": 3, "title": "Read a book", "is_completed": False, "user_id": 2},
]

initial_user = users.copy()
initial_tasks = tasks.copy()

# ID counters
user_id_counter = 3
task_id_counter = 4


def reset_data():
    global users, tasks, user_id_counter, task_id_counter

    users = initial_users = users.copy()
    tasks = initial_tasks = tasks.copy()

    user_id_counter = 3
    task_id_counter = 4

def get_all_users() -> list[dict]:
    return users
    
def get_user_by_id(user_id: int) -> dict | None:
    for user in users:
        if user["id"] == user_id:
            return user
    return none

def create_user(name: str) -> dict:
    global user_id_counter
    new_user = {
        "id" : user_id_counter,
        "name" : name
    }
    users.append(new.user)
    user_id_counter +=

    return new_user


def get_all_tasks() -> list[dict]:
    return tasks

def get_task_by_id(task_id: int) -> dict | None:
    """Ambil task berdasarkan id"""
    # TODO: Cari task by id, return dict atau None
    pass


def get_tasks_by_user(user_id: int) -> list[dict]:
    """Ambil semua task berdasarkan user_id"""
    # TODO: Filter task by user_id
    pass


def create_task(user_id: int, title: str) -> dict:
    """Buat task baru untuk user tertentu"""
    # TODO: Validasi user ada, buat task baru is_completed=False
    pass


def update_task(task_id: int, updates: dict) -> dict:
    """Update task berdasarkan id"""
    # TODO: Update task fields (title/is_completed) berdasarkan id
    pass


def delete_task(task_id: int) -> bool:
    """Hapus task berdasarkan id"""
    # TODO: Hapus task dari list, return True/False
    pass
