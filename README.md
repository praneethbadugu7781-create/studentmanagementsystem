# Student Management System

### Using Django Framework
**Internship Project Demonstration**  
**Organization:** Lineysha and Thevan Software Technologies, Vijayawada  
**Technology Stack:** Python 3.10+, Django 5.x, HTML5, CSS3, Bootstrap 5, SQLite

---

## 📌 Project Overview

The **Student Management System** is a centralized, digital student record management web application built with Django's Model-View-Template (MVT) architecture. Designed to eliminate manual paperwork and spreadsheet inefficiencies, it provides college administrators with a real-time, responsive, and secure dashboard to store, view, search, edit, and delete student records.

---

## 🌟 Key Features

1. **Dashboard & Analytics:**
   - Real-time statistics: Total Students, Unique Courses, Total Records, Active Database (`SQLite`).
   - Dynamic counter animations.
   - Recent Students table with initial-based avatars and quick action buttons.
   - Quick "+ Add Student" access button.

2. **Student Records Directory (`/students/`):**
   - Multi-field backend search: Search across **Full Name**, **Roll Number**, **Email**, **Course**, and **Phone Number**.
   - Clear search reset option.
   - Server-side pagination retaining active search queries.
   - Status & course badges.
   - Action controls: View Profile, Edit Record, Delete Record.

3. **Student CRUD Operations:**
   - **Add Student (`/students/add/`):** Django ModelForm with client-side & server-side validation.
   - **Student Profile (`/students/<id>/`):** Two-column detailed view showing roll number, course, email, phone, created and updated timestamps.
   - **Edit Student (`/students/<id>/edit/`):** Pre-filled form with instant validation.
   - **Delete Student (`/students/<id>/delete/`):** Safe POST-based deletion with confirmation modal dialog.

4. **Notifications & Feedback:**
   - Django Messages Framework integration with auto-dismissing toast notifications.

5. **Django Admin Integration (`/admin/`):**
   - Pre-configured `StudentAdmin` with custom list display, search fields, filtering by course and creation date, and ordering.

6. **Modern Academic UI/UX:**
   - Light aesthetic (pure white cards, soft blue accents, soft lavender pills, soft green/red indicators).
   - Fully responsive for Mobile, Tablet, Laptop, and Desktop.

---

## 🗂️ Core Student Model Schema

| Field Name | Type | Constraints / Details |
| :--- | :--- | :--- |
| `name` | `CharField(max_length=100)` | Full Name of the student |
| `roll_number` | `CharField(max_length=20)` | Unique student roll identifier |
| `email` | `EmailField()` | Valid student email address |
| `course` | `CharField(max_length=100)` | Course / Department program |
| `phone` | `CharField(max_length=15)` | Contact phone number |
| `created_at` | `DateTimeField(auto_now_add=True)` | Record creation timestamp |
| `updated_at` | `DateTimeField(auto_now=True)` | Record modification timestamp |

---

## 📁 Project Directory Structure

```text
seeluu/
├── manage.py
├── db.sqlite3
├── student_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── students/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   └── management/
│       └── commands/
│           ├── __init__.py
│           └── seed_students.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── 404.html
│   ├── 500.html
│   └── students/
│       ├── student_list.html
│       ├── student_detail.html
│       └── student_form.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

---

## 🚀 Quickstart & Setup Guide

### 1. Prerequisites
- Python 3.10 or higher
- Pip package manager

### 2. Apply Migrations
```bash
python manage.py migrate
```

### 3. Seed Sample Student Records (Optional)
```bash
python manage.py seed_students
```

### 4. Run Automated Test Suite
```bash
python manage.py test students
```

### 5. Start Development Server
```bash
python manage.py runserver 8000
```
Then open your browser and visit:
- **Application Dashboard:** `http://127.0.0.1:8000/`
- **Students Directory:** `http://127.0.0.1:8000/students/`
- **Add Student:** `http://127.0.0.1:8000/students/add/`
- **Django Admin:** `http://127.0.0.1:8000/admin/`  
  *(Default Superuser: Username: `admin` | Password: `admin123`)*

---

## 🏢 Organization & Internship Credit

- **Project:** Student Management System
- **Company:** Lineysha and Thevan Software Technologies
- **Location:** Vijayawada
- **Role:** Full Stack Developer – Python Internship
