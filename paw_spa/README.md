# Paw Spa - Pet Grooming Booking System

A Django-based web application for managing pet spa and grooming appointments.

## Features

- Book appointments for pet grooming services
- View and manage bookings
- Custom admin dashboard for booking approvals
- Modern and responsive UI

## Setup Instructions

1. Clone or download this repository
2. Install Python 3.8 or higher if not already installed
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Navigate to the project directory:
   ```
   cd paw_spa
   ```
5. Run database migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```
   python manage.py runserver
   ```
8. Visit http://127.0.0.1:8000 in your web browser

## Admin Access

- Custom admin login: http://127.0.0.1:8000/admin-login/
- Default Django admin: http://127.0.0.1:8000/admin/

## Project Structure

- `/booking` - Main application directory
- `/templates` - HTML templates
- `/static` - Static files (CSS, JS, images)
- `settings.py` - Project settings
- `urls.py` - URL configurations 