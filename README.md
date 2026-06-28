# Django ToDo Application

A fully functional Task Management (ToDo) web application built using Django. This project demonstrates core Django concepts including Custom User Authentication and full CRUD operations using Class-Based Views (CBVs).

## Features
- **User Authentication:** Sign up, Login, and Logout functionality.
- **Secure Data:** Each user can only view, create, update, and delete their own tasks.
- **Task Management (CRUD):** Create, Read, Update, and Delete tasks.
- **Styled UI:** Clean interface built with Bootstrap 5.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
