# Student Management System

A Django-based Student Management System with MySQL database.

This project provides a simple and user-friendly system to manage student records with CRUD operations, search, course filtering, pagination, and student details.

---

## 🚀 Features

- Add new students
- View all students
- View student details
- Edit student information
- Delete students
- Search students
- Filter students by course
- Pagination
- Dashboard statistics
- MySQL database integration
- Environment variable configuration using `.env`
- Secure `.gitignore` configuration

---

## 🛠️ Tech Stack

- Python
- Django
- MySQL
- HTML5
- CSS3
- Django Templates
- python-dotenv
- Git
- GitHub

---

## 📂 Project Structure

```text
StudentManagementSystem/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── home.html
│   │       ├── add_student.html
│   │       ├── student_list.html
│   │       ├── student_detail.html
│   │       ├── edit_student.html
│   │       └── delete_student.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/rishiwebai/StudentManagementSystem.git