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
    for task in tasks:
        if task["id"] == task_id:
            return task
    return none

def get_tasks_by_user(user_id: int) -> list[dict]:
    for tasks in users:
        if tasks ["id"] == user_id:
            return task
    return user

def create_task(user_id: int, title: str) -> dict:
    """Buat task baru untuk user tertentu"""
    global task_id_counter
        if get_user_by_id(user_id) is_none:
            return none

    new_task = {
        "id": task_id_counter,
        "title": title,
        "is_complite": False,
        "user_id": user_id
    }
    task.append(new_task)
    task_id_counter += 1

    return new_task
    


def update_task(task_id: int, updates: dict) -> dict:
    task = get_task_by_id(task_id)
    if task is none:
        return none

    task.update(updates)
    return task
    """Update task berdasarkan id"""
    # TODO: Update task fields (title/is_completed) berdasarkan id


def delete_task(task_id: int) -> bool:
    """Hapus task berdasarkan id"""
    for task in task:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False
