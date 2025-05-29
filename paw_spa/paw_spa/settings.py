from pathlib import Path
import pymysql

# This line allows Django to connect to MySQL using the PyMySQL library
pymysql.install_as_MySQLdb()

# Set the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key for encryption — keep this secret in production
SECRET_KEY = 'django-insecure-...'

# DEBUG should be True for development, False for production
DEBUG = True

# Allowed hosts list (empty for local development)
ALLOWED_HOSTS = []

# Django applications that are installed and used in the project
INSTALLED_APPS = [
    'django.contrib.admin',       # Admin interface
    'django.contrib.auth',        # User authentication
    'django.contrib.contenttypes',# Content type system
    'django.contrib.sessions',    # Session management
    'django.contrib.messages',    # Flash messages
    'django.contrib.staticfiles', # Static file support
    'booking',                    # Our custom app for managing bookings
]

# Middleware are functions that process requests/responses globally
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'paw_spa.urls'

# Template engine settings (for rendering HTML pages)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add custom template directories here
        'APP_DIRS': True,  # Looks for templates inside app folders
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI entry point for deploying the app on a web server
WSGI_APPLICATION = 'paw_spa.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validators for user accounts
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Language and time zone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static file (CSS, JS, images) settings
STATIC_URL = 'static/'

# Default auto primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

