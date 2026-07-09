# CTS Weekly Task - Week 4 (Module 5)

## Objective

Implement JWT Authentication using FastAPI.

---

## Features

- User Registration
- User Login
- JWT Token Generation
- Protected Route
- Logout Endpoint
- Swagger Documentation

---

## Technologies

- Python
- FastAPI
- SQLAlchemy
- JWT
- SQLite

---

## Project Structure

```
jwt_auth/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── requirements.txt
└── README.md
```

---

## Run

```bash
pip install -r requirements.txt

uvicorn main:app --reload
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register User |
| POST | /login | User Login |
| GET | /profile | Protected Route |
| POST | /logout | Logout User |

---

## Key Learning

Learned to implement JWT-based authentication in FastAPI with protected API routes and token-based authorization.

---

## Outcome

Successfully implemented JWT authentication with login, logout, and protected routes using FastAPI.