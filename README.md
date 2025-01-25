 Django User Authentication Project

This is a Django-based project that implements basic user authentication features such as signup, login, logout, and password reset. 
It uses a custom user model for the project and includes functionality for users to sign up, log in, log out, and reset their passwords.

 Features

- User Authentication: Allows users to sign up, log in, log out, and reset their password.
- Custom User Model: The default Django `User` model is replaced with a custom `CustomUser` model.
- Password Reset: Users can reset their password via email (using Django’s built-in password reset functionality).
- Django Views: Implements custom and built-in views like the `LogoutView` and `SignupView`.
- CSRF Protection: CSRF tokens are included in the forms for added security.

Prerequisites

Before running the project, make sure you have the following installed:

- Python (>= 3.6)
- Django (>= 3.x)
- Git (for version control)
- A text editor or IDE (e.g., VSCode, PyCharm)

 Installation

 1. Clone the repository
git clone https://github.com/your-username/django-project.git
cd django-project

2.Setup virtual environment
python3 -m venv venv
`venv\Scripts\activate`

3. Install dependencies

4. Run migrations to setup your database schema
python manage.py makemigrations
python manage.py migrate

5. To interact with the admin panel and test the authentication system, create a superuser
python manage.py createsuperuser

6. Run the development server
python manage.py runserver





