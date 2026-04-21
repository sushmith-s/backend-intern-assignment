# backend-intern-assignment
# 🚀 Backend Intern Assignment – Task Management API

A full-stack Task Management application built using Django REST Framework (backend) and React (frontend), featuring JWT authentication, role-based access control, and API documentation.

---

# 📌 Features

## 🔐 Authentication

* User Registration API
* User Login with JWT Authentication
* Secure password hashing

## 👥 Role-Based Access

* **Admin** → Can view all tasks
* **User** → Can view and manage only their tasks

## 📋 Task Management (CRUD)

* Create Task
* Get Tasks
* Update Task
* Delete Task

## 📡 API Design

* RESTful endpoints (`/api/v1/...`)
* Proper HTTP status codes
* Clean and modular structure

## 📄 API Documentation

* Swagger UI (OpenAPI 3.0) using drf-spectacular

## 🖥️ Frontend

* Login & Register pages
* Dashboard with task list
* Add tasks functionality
* Connected to backend APIs

---

# 🛠️ Tech Stack

## Backend

* Python
* Django
* Django REST Framework
* SimpleJWT (Authentication)
* SQLite (Development DB)

## Frontend

* React.js
* Axios
* React Router

---

# ⚙️ Setup Instructions

## 🔹 Backend Setup

```bash
# Clone repo
git clone <your-repo-link>
cd backend-intern-assignment

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

## 🔹 Frontend Setup

```bash
cd frontend

npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

# 🔑 API Endpoints

## Authentication

* `POST /api/v1/auth/register/`
* `POST /api/v1/auth/login/`

## Tasks

* `GET /api/v1/tasks/`
* `POST /api/v1/tasks/`
* `PUT /api/v1/tasks/{id}/`
* `DELETE /api/v1/tasks/{id}/`

---

# 📄 Swagger Documentation

Access Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

Use:

```
Authorize → Bearer <your_token>
```

---

# 🧠 Database

* SQLite used for development
* Easily scalable to PostgreSQL for production

---

# 🔐 Security

* JWT Authentication
* Password hashing
* Role-based authorization
* Protected API endpoints

---

# 📈 Scalability Approach

This project can be scaled using:

* PostgreSQL (production database)
* Redis (caching layer)
* Docker (containerization)
* Load balancing (Nginx)
* Microservices architecture (future expansion)

---

# 🎯 Project Structure

```
backend-intern-assignment/
│
├── accounts/        # Authentication & User model
├── tasks/           # Task APIs
├── core/            # Settings & URLs
├── frontend/        # React app
└── db.sqlite3
```

---

# ✅ Completed Requirements

* ✔ Authentication system
* ✔ Role-based access control
* ✔ CRUD APIs
* ✔ API documentation (Swagger)
* ✔ Frontend integration
* ✔ Database integration

---

# 🚀 Future Improvements

* Task update UI
* Delete task button
* UI styling (Tailwind)
* Deployment (Render / Railway)
* Docker setup

---

# 👨‍💻 Author

Sushmith S

---

# ⭐ Final Note

This project demonstrates:

* Backend API development
* Authentication & authorization
* Full-stack integration
* Scalable architecture thinking
