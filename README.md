# برنامه مدیریت کارها با جنگو (Django ToDo Application)

[English Version Below](#django-todo-application-english)

یک وب‌اپلیکیشن کامل برای مدیریت کارها (ToDo) که با فریم‌ورک جنگو توسعه یافته است. این پروژه مفاهیم کلیدی جنگو مانند احراز هویت سفارشی کاربران و عملیات کامل CRUD را با استفاده از Class-Based Views (CBVs) نمایش می‌دهد.

## ویژگی‌ها
- **احراز هویت کاربران:** قابلیت ثبت‌نام، ورود و خروج ایمن از حساب کاربری.
- **امنیت داده‌ها:** هر کاربر فقط می‌تواند کارهای مربوط به خودش را مشاهده، ایجاد، ویرایش و حذف کند.
- **مدیریت کارها (CRUD):** امکان ساخت، خواندن، بروزرسانی و حذف کامل تسک‌ها.
- **رابط کاربری شیک:** طراحی تمیز و واکنش‌گرا با استفاده از بوت‌استرپ ۵ (Bootstrap 5).

## نصب و راه‌اندازی

۱. مخزن پروژه را کلون کنید:
   ```bash
   git clone <your-repository-url>
   ```
۲. محیط مجازی را ساخته و فعال کنید:
   ```bash
   python -m venv venv
   # در ویندوز:
   venv\Scripts\activate
   ```
۳. نیازمندی‌های پروژه را نصب کنید:
   ```bash
   pip install -r requirements.txt
   ```
۴. مایگریشن‌ها را اجرا کرده و سرور را روشن کنید:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

<a name="django-todo-application-english"></a>
# Django ToDo Application (English)

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
