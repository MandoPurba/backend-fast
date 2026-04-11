task-forge-lite/TASK.md
```

```markdown
# TaskForge Lite - Daftar Tugas

Tugas ini bertujuan untuk melatih pemahaman tentang **layered architecture**, **Flask API**, dan **CRUD operations** tanpa database.

## Petunjuk Pengerjaan

1. Baca setiap file untuk memahami apa yang perlu dilakukan
2. Setiap fungsi/kelas memiliki `# TODO: Implementasi`
3. Ganti `pass` dengan implementasi yang benar
4. Jalankan test untuk memverifikasi implementasi
5. Tests harus green semua sebelum dianggap selesai

---

## Task 1: In-Memory Database Layer

**File:** `database/inmemory.py`

Implementasikan fungsi-fungsi berikut:

### 1.1 `reset_data()`
- Mereset semua data ke kondisi awal (fake data)
- Mengembalikan `users`, `tasks`, `user_id_counter`, `task_id_counter` ke nilai awal

### 1.2 `get_all_users() -> list[dict]`
- Mengembalikan semua user dari list `users`
- Return: `list[dict]`

### 1.3 `get_user_by_id(user_id: int) -> dict | None`
- Mencari user berdasarkan `user_id`
- Return: `dict` user jika ditemukan, `None` jika tidak

### 1.4 `create_user(name: str) -> dict`
- Membuat user baru dengan auto-increment ID
- Menyimpan ke list `users`
- Return: `dict` user yang baru dibuat

### 1.5 `get_all_tasks() -> list[dict]`
- Mengembalikan semua task dari list `tasks`
- Return: `list[dict]`

### 1.6 `get_task_by_id(task_id: int) -> dict | None`
- Mencari task berdasarkan `task_id`
- Return: `dict` task jika ditemukan, `None` jika tidak

### 1.7 `get_tasks_by_user(user_id: int) -> list[dict]`
- Mengembalikan semua task milik user tertentu
- Return: `list[dict]`

### 1.8 `create_task(user_id: int, title: str) -> dict`
- Membuat task baru dengan auto-increment ID
- Default `is_completed = False`
- Menyimpan ke list `tasks`
- Return: `dict` task yang baru dibuat
- **Validasi:** User harus ada

### 1.9 `update_task(task_id: int, updates: dict) -> dict`
- Mengupdate task berdasarkan `task_id`
- `updates` bisa berisi `title` dan/atau `is_completed`
- Return: `dict` task yang sudah diupdate
- **Validasi:** Task harus ada

### 1.10 `delete_task(task_id: int) -> bool`
- Menghapus task dari list `tasks`
- Return: `True` jika berhasil, `False` jika tidak ditemukan

---

## Task 2: User Service Layer

**File:** `services/user_service.py`

Implementasikan class `UserService` berikut:

### 2.1 `create_user(name: str) -> dict`
- Membuat user baru melalui database layer
- **Validasi:** `name` tidak boleh kosong
- Return: `dict` user yang dibuat

### 2.2 `get_user_by_id(user_id: int) -> dict`
- Mengambil user berdasarkan ID
- **Validasi:** User harus ada, jika tidak抛出 `ValueError`
- Return: `dict` user

### 2.3 `get_all_users() -> list[dict]`
- Mengambil semua user
- Return: `list[dict]`

---

## Task 3: Task Service Layer

**File:** `services/task_service.py`

Implementasikan class `TaskService` berikut:

### 3.1 `create_task(user_id: int, title: str) -> dict`
- Membuat task baru
- **Validasi:**
  - User harus ada, jika tidak抛出 `ValueError`
  - `title` tidak boleh kosong, jika tidak抛出 `ValueError`
  - Title tidak boleh duplicate untuk user yang sama, jika tidak抛出 `ValueError`
  - Maksimal 10 task per user, jika tidak抛出 `ValueError`
- Return: `dict` task yang dibuat

### 3.2 `get_all_tasks() -> list[dict]`
- Mengambil semua task
- Return: `list[dict]`

### 3.3 `get_tasks_by_user(user_id: int) -> list[dict]`
- Mengambil semua task berdasarkan user_id
- Return: `list[dict]`

### 3.4 `get_task_by_id(task_id: int) -> dict`
- Mengambil task berdasarkan ID
- **Validasi:** Task harus ada, jika tidak抛出 `ValueError`
- Return: `dict` task

### 3.5 `mark_task_completed(task_id: int) -> dict`
- Menandai task sebagai completed
- **Validasi:** Task harus ada, jika tidak抛出 `ValueError`
- Return: `dict` task yang sudah diupdate

### 3.6 `delete_task(task_id: int) -> bool`
- Menghapus task
- **Validasi:** Task harus ada, jika tidak抛出 `ValueError`
- Return: `True` jika berhasil

---

## Task 4: User Handler Layer (API)

**File:** `handlers/user_handler.py`

Implementasikan Flask endpoint handlers berikut:

### 4.1 `create_user_handler() -> tuple`
- Endpoint: `POST /users`
- Body: `{"name": str}`
- **Validasi:**
  - `name` harus ada dan tidak kosong
- Response:
  - `201` dengan user data jika berhasil
  - `400` dengan error message jika validasi gagal

### 4.2 `list_users_handler() -> tuple`
- Endpoint: `GET /users`
- Response: `200` dengan list semua user

### 4.3 `get_user_handler(user_id: int) -> tuple`
- Endpoint: `GET /users/<user_id>`
- Response:
  - `200` dengan user data jika ditemukan
  - `404` dengan error message jika tidak ditemukan

---

## Task 5: Task Handler Layer (API)

**File:** `handlers/task_handler.py`

Implementasikan Flask endpoint handlers berikut:

### 5.1 `create_task_handler() -> tuple`
- Endpoint: `POST /tasks`
- Body: `{"user_id": int, "title": str}`
- **Validasi:**
  - User harus ada
  - `title` tidak boleh kosong
  - Title tidak boleh duplicate untuk user yang sama
  - Maksimal 10 task per user
- Response:
  - `201` dengan task data jika berhasil
  - `400` dengan error message jika validasi gagal
  - `404` jika user tidak ditemukan

### 5.2 `get_all_tasks_handler() -> tuple`
- Endpoint: `GET /tasks`
- Response: `200` dengan list semua task

### 5.3 `get_task_by_id_handler(task_id: int) -> tuple`
- Endpoint: `GET /tasks/<task_id>`
- Response:
  - `200` dengan task data jika ditemukan
  - `404` jika tidak ditemukan

### 5.4 `get_tasks_by_user_handler(user_id: int) -> tuple`
- Endpoint: `GET /tasks/user/<user_id>`
- Response: `200` dengan list task user tersebut

### 5.5 `mark_task_completed_handler(task_id: int) -> tuple`
- Endpoint: `PATCH /tasks/<task_id>/complete`
- Response:
  - `200` dengan task data jika berhasil
  - `404` jika task tidak ditemukan

### 5.6 `delete_task_handler(task_id: int) -> tuple`
- Endpoint: `DELETE /tasks/<task_id>`
- Response:
  - `200` dengan message jika berhasil
  - `404` jika task tidak ditemukan

---

## Urutan Pengerjaan

Disarankan untuk mengerjakan dalam urutan berikut:

```
1. database/inmemory.py        → Test: test_database.py
2. services/user_service.py     → Test: (bagian dari test_handlers.py)
3. services/task_service.py     → Test: (bagian dari test_handlers.py)
4. handlers/user_handler.py     → Test: test_handlers.py
5. handlers/task_handler.py    → Test: test_handlers.py
```

## Verifikasi

Jalankan semua test untuk memverifikasi implementasi:

```bash
uv run pytest tests/ -v
```

Semua test harus **PASSED** (green).

## Contoh Error Handling

```python
# Jika validasi gagal, raise ValueError dengan message yang jelas
if not name:
    raise ValueError("Name cannot be empty")

# Di handler, catch ValueError dan return 400/404
try:
    user = user_service.get_user_by_id(user_id)
except ValueError:
    return {"error": "User not found"}, 404
```

---

## Expected Results

### After Task 1 (Database Layer)
```
tests/test_database.py::TestGetAllUsers PASSED
tests/test_database.py::TestGetUserById PASSED
tests/test_database.py::TestCreateUser PASSED
tests/test_database.py::TestGetAllTasks PASSED
tests/test_database.py::TestGetTaskById PASSED
tests/test_database.py::TestGetTasksByUser PASSED
tests/test_database.py::TestCreateTask PASSED
tests/test_database.py::TestUpdateTask PASSED
tests/test_database.py::TestDeleteTask PASSED
tests/test_database.py::TestResetData PASSED
```

### After All Tasks (Full Integration)
```
tests/test_handlers.py::TestHealthCheck PASSED
tests/test_handlers.py::TestUserHandler PASSED
tests/test_handlers.py::TestTaskHandler PASSED
tests/test_handlers.py::TestEdgeCases PASSED
```
