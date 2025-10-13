# 📚 Library Management System API  

This project is a **requirement project for graduation** in the **ALX Backend Engineering program**.  
It is a **Library Management System API** built with **Django + Django REST Framework (DRF)**.  

The goal is to provide a backend system that allows **librarians** to manage books and users, while **students** can borrow and return books with proper tracking.  

---

## 🚀 Features Implemented  

### 🏗️ Week 1: Project Setup & Models
- Created **Django project** (`library_api`) and application.
- Configured **virtual environment** and `requirements.txt`.
- Designed database models:
  - **User** → Custom user model with fields: `username`, `email`, `password`, `date_of_membership`, `role` (student/librarian), and `active_status`.
  - **Book** → `title`, `author`, `ISBN (unique)`, `published_date`, `available_copies`.
  - **Category** → Optional classification for books.
  - **Transaction** → Connects users with books and records `borrow`/`return` dates.
- Ran initial **migrations** successfully.
- Registered all models in the **Django Admin Panel**.
- Verified functionality by creating and managing books in admin.

---

### ⚙️ Week 2: CRUD APIs & Authentication
- Added **serializers** for all models.
- Implemented **CRUD APIs** using DRF ViewSets:
  - `/api/users/` → User management  
  - `/api/books/` → Book management  
  - `/api/categories/` → Book categories  
  - `/api/transactions/` → Borrowing records  
- Configured **DefaultRouter** for automatic route handling.
- Implemented **authentication system**:
  - `POST /api/register/` → Register a new user  
  - `POST /api/login/` → Login and receive an authentication token  
  - `POST /api/logout/` → Logout the user  
- Updated `settings.py` with authentication and permissions.
- Confirmed API root displays registered endpoints:
  ```json
  {
    "users": "http://127.0.0.1:8000/api/users/",
    "books": "http://127.0.0.1:8000/api/books/",
    "transactions": "http://127.0.0.1:8000/api/transactions/",
    "categories": "http://127.0.0.1:8000/api/categories/"
  }

🔄 Week 3: Borrow/Return Logic, Permissions & Testing
✅ Key Updates

Implemented borrow and return functionality under the TransactionViewSet:

POST /api/transactions/{id}/borrow/ → Borrow a book (students only)

POST /api/transactions/{id}/return_book/ → Return a borrowed book

Added validation rules:

Only students can borrow books.

Books with 0 available copies cannot be borrowed.

Borrowed books can only be returned once.

Updated permissions:

Librarians: Can add, edit, or delete books.

Students: Can view and borrow/return books.

Improved querysets:

Librarians see all transactions.

Students only see their own transaction history.

Added custom permission class IsLibrarian for role-based access control.

Verified all endpoints through DRF’s web interface and Postman.

🧪 Testing

Confirmed API actions:

Borrowed books reduce available copies.

Returned books restore available copies.

Invalid or duplicate borrow requests return proper HTTP status codes.

Ran:

python manage.py check
python manage.py runserver


✅ No errors were detected.

🧰 Tech Stack

Python 3.12+

Django 5.2.7

Django REST Framework 3.16.1

SQLite3 (default database)

Token Authentication

🛠️ Setup Instructions

Clone this repository:

git clone https://github.com/IbrahimAdegboye/library-mgtsystem.git


Navigate into the project:

cd library-mgtsystem


Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start the server:

python manage.py runserver