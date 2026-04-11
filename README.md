# TaskForge Lite

Backend service sederhana untuk mengelola task (to-do) tanpa menggunakan database. Dibuat untuk tujuan pembelajaran dengan fokus pada **layered architecture** dan **Flask API**.

## Arsitektur

```
task-forge-lite/
├── database/                 # Data Access Layer
│   └── inmemory.py           # In-memory database (fake data)
├── services/                 # Business Logic Layer
│   ├── user_service.py       # User service
│   └── task_service.py       # Task service
├── handlers/                 # API Layer
│   ├── user_handler.py       # User Flask blueprint
│   └── task_handler.py       # Task Flask blueprint
├── tests/                    # Unit Tests
│   ├── test_database.py      # Tests untuk database layer
│   └── test_handlers.py      # Tests untuk Flask API
├── app.py                    # Flask application factory
└── pyproject.toml            # Dependencies
```

## Setup Project

### Prerequisites

- Python 3.10 atau lebih baru
- uv (package manager)

### Cara Install uv

```bash
# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### Mac / Linux

1. **Buka Terminal**

2. **Clone project ini**, lalu masuk ke folder project:
```bash
git clone https://github.com/MandoPurba/backend-fast.git
# atau (SSH)
git clone git@github.com:MandoPurba/backend-fast.git
cd backend-fast
```

3. **Install dependencies dengan uv:**
```bash
uv sync
```

4. **(Opsional) Aktifkan virtual environment:**
```bash
source .venv/bin/activate
```

5. **Verify installation:**
```bash
python --version
python -c "import flask; print(flask.__version__)"
```

### Windows

1. **Buka Command Prompt atau PowerShell**

2. **Clone project ini**, lalu masuk ke folder project:
```powershell
git clone https://github.com/MandoPurba/backend-fast.git
# atau (SSH)
git clone git@github.com:MandoPurba/backend-fast.git
cd backend-fast
```

3. **Install dependencies dengan uv:**
```powershell
uv sync
```

4. **(Opsional) Aktifkan virtual environment:**
```powershell
.venv\Scripts\activate
```

5. **Verify installation:**
```powershell
python --version
python -c "import flask; print(flask.__version__)"
```

## Menjalankan Tests

### Menggunakan uv run

```bash
# Jalankan semua tests
uv run pytest tests/ -v

# Jalankan hanya database tests
uv run pytest tests/test_database.py -v

# Jalankan hanya handler tests
uv run pytest tests/test_handlers.py -v

# Jalankan dengan coverage
uv run pytest tests/ -v --cov
```

### Menggunakan uv test

```bash
# Jalankan semua tests
uv test

# Jalankan dengan verbose
uv test -- -v

# Jalankan hanya database tests
uv test tests/test_database.py

# Jalankan hanya handler tests
uv test tests/test_handlers.py
```

## Menjalankan API

```bash
# Menggunakan uv run
uv run python app.py

# Atau aktifkan venv terlebih dahulu
source .venv/bin/activate  # Mac / Linux
# atau
.venv\Scripts\activate      # Windows
python app.py
```

API akan berjalan di `http://localhost:5000`

## API Endpoints

### Health Check
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | List all users |
| POST | `/users` | Create user |
| GET | `/users/<id>` | Get user by ID |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List all tasks |
| POST | `/tasks` | Create task |
| GET | `/tasks/<id>` | Get task by ID |
| GET | `/tasks/user/<user_id>` | Get tasks by user |
| PATCH | `/tasks/<id>/complete` | Mark task completed |
| DELETE | `/tasks/<id>` | Delete task |

## Data Structure

### User
```json
{
  "id": 1,
  "name": "Alice"
}
```

### Task
```json
{
  "id": 1,
  "title": "Buy groceries",
  "is_completed": false,
  "user_id": 1
}
```

## Constraints

- Title tidak boleh kosong
- User harus ada sebelum membuat task
- Maksimal 10 task per user
- Tidak boleh duplicate title untuk user yang sama

## Layered Architecture

```
┌─────────────┐
│  Handlers   │  ← API Layer (Flask Blueprints)
│  (API)      │
└──────┬──────┘
       │
┌──────▼──────┐
│  Services    │  ← Business Logic Layer
└──────┬──────┘
       │
┌──────▼──────┐
│  Database    │  ← Data Access Layer (In-Memory)
│  (inmemory)  │
└─────────────┘
```

## Contoh Request

### Create User
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Charlie"}'
```

### Create Task
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "title": "Buy groceries"}'
```

### Get All Tasks
```bash
curl http://localhost:5000/tasks
```

### Mark Task Completed
```bash
curl -X PATCH http://localhost:5000/tasks/1/complete
```

### Delete Task
```bash
curl -X DELETE http://localhost:5000/tasks/1
```

## Troubleshooting

### `uv: command not found`
Install uv terlebih dahulu:
```bash
# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex
```

### Permission Error (Mac / Linux)
```bash
chmod +x .venv/bin/activate
```

### Flask import error
Pastikan dependencies sudah terinstall:
```bash
uv sync
source .venv/bin/activate  # Mac / Linux
# atau
.venv\Scripts\activate     # Windows
```
