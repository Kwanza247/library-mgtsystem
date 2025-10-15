# 📚 Library Management System API  

This project is a **requirement for graduation** in the **ALX Backend Engineering Program**.  
It is a **Library Management System API** built with **Django + Django REST Framework (DRF)**.  

The goal is to provide a backend system that allows **librarians** to manage books and users, while **students** can borrow and return books with proper tracking.  

---

## 🚀 Features Implemented  

### 🏗️ Week 1: Project Setup & Models
- Created the **Django project** (`library_api`) and application.
- Configured **virtual environment** and `requirements.txt`.
- Designed database models:
  - **User** → Custom model with `username`, `email`, `password`, `date_of_membership`, `role` (student/librarian), and `active_status`.
  - **Book** → Fields include `title`, `author`, `ISBN` (unique), `published_date`, and `available_copies`.
  - **Category** → Optional classification for books.
  - **Transaction** → Connects users and books; tracks `borrow_date` and `return_date`.
- Ran initial **migrations** successfully.
- Registered models in the **Django Admin Panel**.
- Verified basic functionality through the admin interface.

---

### ⚙️ Week 2: CRUD APIs & Authentication
- Added **serializers** for all models.
- Implemented **CRUD APIs** using DRF ViewSets:
  - `/api/users/` → User management  
  - `/api/books/` → Book management  
  - `/api/categories/` → Book categories  
  - `/api/transactions/` → Borrowing records  
- Configured `DefaultRouter` for automatic route registration.
- Added **authentication system**:
  - `POST /api/register/` → Register a new user  
  - `POST /api/login/` → Login and receive authentication token  
  - `POST /api/logout/` → Logout user  
- Updated `settings.py` with token and session authentication.
- Confirmed API Root returns registered endpoints:
  ```json
  {
    "users": "http://127.0.0.1:8000/api/users/",
    "books": "http://127.0.0.1:8000/api/books/",
    "transactions": "http://127.0.0.1:8000/api/transactions/",
    "categories": "http://127.0.0.1:8000/api/categories/"
  }

**Week 3: Borrow/Return Logic, Permissions & Testing**

Key Updates

Implemented borrow and return functionality under TransactionViewSet:

POST /api/transactions/{id}/borrow/ → Borrow a book (students only)

POST /api/transactions/{id}/return_book/ → Return a borrowed book

Added validation rules:

Only students can borrow books.

Books with 0 available copies cannot be borrowed.

Borrowed books can only be returned once.

Updated permissions:

Librarians → Can add, edit, or delete books.

Students → Can view and borrow/return books.

Created custom permission class IsLibrarian for role-based access control.

Improved querysets:

Librarians see all transactions.

Students only see their own borrowing history.

Verified endpoints through DRF’s web interface and Postman.

**Testing & Validation**

Borrowed books reduce available copies.

Returned books restore available copies.

Invalid or duplicate borrow requests return proper HTTP status codes.

Ran:

python manage.py check
python manage.py runserver


 No errors detected.

**Tech Stack**

Python 3.12+

Django 5.2.7

Django REST Framework 3.16.1

SQLite3 (default database)

Token Authentication

**Setup Instructions**

Clone this repository
git clone https://github.com/IbrahimAdegboye/library-mgtsystem.git
cd library-mgtsystem

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

**Install dependencies**
pip install -r requirements.txt

**Run migrations**
Run migrations
python manage.py migrate

start the development runserver
**python manage.py runserver**
