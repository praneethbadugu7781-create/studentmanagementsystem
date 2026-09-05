"""
Django settings for student_management project.
Production-ready configuration supporting Vercel, Render, PythonAnywhere, Railway.
"""

import os
import shutil
from pathlib import Path
try:
    import dj_database_url
except ImportError:
    dj_database_url = None
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-lvjrrc56umr&dcxc3faqfl7obstael-ibcu!^@tm@vo5ipk5i9'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'https://*.onrender.com',
    'https://*.railway.app',
    'https://*.pythonanywhere.com',
    'http://127.0.0.1',
    'http://localhost',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'students',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'student_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'student_management.wsgi.application'

# Database configuration
# 1. If DATABASE_URL is provided (e.g. Postgres / Supabase / Neon / Render), use it
# 2. Otherwise default to SQLite (supports serverless /tmp on Vercel and persistent SQLite on Render)
raw_db_url = os.environ.get('DATABASE_URL', '').strip()
if raw_db_url and dj_database_url:
    # Auto-sanitize in case user copied the "psql '...'" snippet directly from Neon / CLI
    if raw_db_url.startswith('psql'):
        raw_db_url = raw_db_url[4:].strip()
    raw_db_url = raw_db_url.strip("'\"` ")

    try:
        db_config = dj_database_url.parse(
            raw_db_url,
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        )
        if 'OPTIONS' in db_config and isinstance(db_config['OPTIONS'], dict):
            db_config['OPTIONS'].pop('channel_binding', None)
        DATABASES = {'default': db_config}
    except Exception as e:
        print(f"Failed to parse DATABASE_URL ({e}), falling back to SQLite")
        if os.environ.get('VERCEL'):
            DB_PATH = Path('/tmp/db.sqlite3')
        else:
            DB_PATH = BASE_DIR / 'db.sqlite3'
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': DB_PATH,
            }
        }
else:
    if os.environ.get('VERCEL'):
        DB_PATH = Path('/tmp/db.sqlite3')
    else:
        DB_PATH = BASE_DIR / 'db.sqlite3'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DB_PATH,
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage configuration
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Messages tag mapping for Bootstrap 5
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
