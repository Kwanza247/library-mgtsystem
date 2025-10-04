#  Library Management System API  

This project is a **requirement project for graduation** in the ALX Backend Engineering program.  
It is a **Library Management System API** built with **Django + Django REST Framework (DRF)**.  

The goal is to provide a backend system that allows **admins** to manage books and users, while **members** can borrow and return books with proper tracking.  

---

##  Features Implemented (Week 1 & 2)

###  Week 1: Project Setup & Models
- Created **Django project** (`library_api`) and application.
- Configured **virtual environment** and requirements file.
- Designed database models:
  - **User** → Custom user model with fields: username, email, password, date_of_membership, role (student/librarian), and active_status.
  - **Book** → title, author, ISBN (unique), published_date, available_copies.
  - **Category** → optional classification for books.
  - **Transaction** → connects users with books and records borrow/return dates.
- Ran initial **migrations** successfully.
- Registered all models in the **Django Admin Panel**.
- Verified functionality by creating a book entry in admin.

---

### ✅ Week 2: CRUD APIs & Authentication
- Added **serializers** for all models.
- Implemented **CRUD APIs** using DRF ViewSets:
  - `/api/users/` → user management
  - `/api/books/` → book management
  - `/api/categories/` → book categories
  - `/api/transactions/` → borrowing records
- Configured **DefaultRouter** for automatic route handling.
- Implemented **authentication system**:
  - `POST /api/register/` → register a new user  
  - `POST /api/login/` → login and get token/session  
  - `POST /api/logout/` → logout user  
- Updated `settings.py` with authentication and permissions.
- Confirmed API root displays registered endpoints:
  ```json
  {
    "users": "http://127.0.0.1:8000/api/users/",
    "books": "http://127.0.0.1:8000/api/books/",
    "transactions": "http://127.0.0.1:8000/api/transactions/",
    "categories": "http://127.0.0.1:8000/api/categories/"
  }
