# Fundoo Notes API
A FastAPI-based backend application for managing users and notes with a clean architecture, structured logging, and database integration.

## Features
- User Management (Create, Read, Update, Delete)
- Notes Management (CRUD operations)
- Data validation using Pydantic schemas
- SQLAlchemy ORM for database operations
- Structured logging with Loguru
- FastAPI for high-performance APIs
- Modular project structure (routes, services, models)

## Tech Stack
### Backend Framework
- FastAPI – High-performance Python web framework for building APIs

### Database & ORM
- SQLAlchemy – ORM for database operations
- Microsoft SQL Server / Any RDBMS – Relational database (based on your setup)

### Data Validation
- Pydantic – Schema validation and data parsing

### Logging
- Loguru – Structured and readable logging

### Server
- Uvicorn – ASGI server to run FastAPI applications

### Environment & Configuration
- Python Dotenv (.env) – Manage environment variables

### Development Tools
- Python 3.x
- Virtual Environment (.venv)

## Project Structure
```
fundoo-notes
|
|-- src/
|   |
|   |-- config/
|   |   |-- database.py             # DB connection setup
|   |   |-- logger.py               # Logging configuration
|   |   |-- logging_middleware.py   # Request logging middleware
|   |
|   |-- models/              # SQLAlchemy models
|   |   |-- note.py
|   |   |-- user.py
|   |
|   |-- routes/              # API routes
|   |   |-- note_routes.py
|   |   |-- user_routes.py
|   |
|   |-- schemas/             # Pydantic schemas
|   |   |-- note_schema.py
|   |   |-- user_schema.py
|   |
|   |-- services/            # Business logic
|   |   |-- note_service.py
|   |   |-- user_service.py
|   |
|   |-- util/
|   |   |-- dependencies.py  # DB dependency injection
|   |
|   |-- main.py              # Entry point of the application
|
|-- logs/
|   |-- app.log     # Application logs
|
|-- .venv/      # Virtual environment
|-- .env        # Environment variables
|-- README.md
|-- requirements.txt
|-- .gitignore
```

## Installation & Setup
### 1 Clone the repository
```
git clone https://github.com/vilas-kr/fundoo-notes.git
cd fundoo-notes
```

### 2 Create virtual environment
```
python -m venv .venv
```
Activate it:
- Windows:
```
.venv\Scripts\activate
```
- Linux/Mac:
```
source .venv/bin/activate
```

### 3 Install dependencies
```
pip install -r requirements.txt
```

### 4 Configure environment variables
Create .env file:
```
USER_NAME = 'username'
PASSWORD = 'password'
IP = 'localhost'
PORT_NUMBER = 1433
DATABASE = 'fundoo_notes'
```

### 5 Running the Application
```
uvicorn src.main:app --reload
```

### API Access
Base URL:
```
http://127.0.0.1:8000
```

Swagger Docs:
```
http://127.0.0.1:8000/docs
```

## Logging
- Logs are stored in:
```
logs/app.log
```
Includes:
- Request logs
- Error logs
- Structured logging with metadata (user_id, note_id)

## Future Improvements
- JWT Authentication
- User authorization (own notes only)
- Pagination & filtering
- Unit & integration tests
- Docker support
- Deployment (AWS / EC2)

## Author
```
Name: Vilas K R
GitHub: https://github.com/vilas-kr
```

## Note
- Make sure your database is running before starting the server
- Update connection string in .env
