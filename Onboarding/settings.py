"""
Django settings for Onboarding project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path
import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / 'env/django' / os.environ.get('ENV_FILE', default='.env.dev'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    "corsheaders",
    'drf_yasg',

    'users.apps.UsersConfig',
    'welcomejorney.apps.WelcomejorneyConfig',
    'notifications.apps.NotificationsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_TRUSTED_ORIGINS=env.tuple('CSRF_TRUSTED_ORIGINS',default=('http://127.0.0.1',))
CORS_ALLOW_ALL_ORIGINS = env.bool('CORS_ALLOW_ALL_ORIGINS')
CORS_ALLOW_CREDENTIALS = env.bool('CORS_ALLOW_CREDENTIALS')

ROOT_URLCONF = env.str('ROOT_URLCONF')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = env.str('WSGI_APPLICATION')


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {

    'default': env.db_url('MYSQL_URL')

}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': env.tuple('DEFAULT_AUTHENTICATION_CLASSES')

}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = env.str('LANGUAGE_CODE')

TIME_ZONE = env.str('TIME_ZONE')

USE_I18N = env.bool('USE_I18N')

USE_TZ = env.bool('USE_TZ')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = env.str('STATIC_URL')
STATIC_ROOT = os.path.join(BASE_DIR, env.str('STATIC_ROOT'))

MEDIA_URL = env.str('MEDIA_URL')
MEDIA_ROOT = BASE_DIR / env.str('MEDIA_ROOT')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = env.str('DEFAULT_AUTO_FIELD')

AUTH_USER_MODEL = env.str('AUTH_USER_MODEL')


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        days=env.int('ACCESS_TOKEN_LIFETIME')),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        days=env.int('REFRESH_TOKEN_LIFETIME')),
    'ROTATE_REFRESH_TOKENS': env.bool('ROTATE_REFRESH_TOKENS'),
    'BLACKLIST_AFTER_ROTATION': env.bool('BLACKLIST_AFTER_ROTATION'),
    'UPDATE_LAST_LOGIN': env.bool('UPDATE_LAST_LOGIN'),

    'ALGORITHM': env.str('ALGORITHM'),
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': env.tuple('AUTH_HEADER_TYPES'),
    'AUTH_HEADER_NAME': env.str('AUTH_HEADER_NAME'),
    'USER_ID_FIELD': env.str('USER_ID_FIELD'),
    'USER_ID_CLAIM': env.str('USER_ID_CLAIM'),
    'USER_AUTHENTICATION_RULE': env.str('USER_AUTHENTICATION_RULE'),

    'AUTH_TOKEN_CLASSES': env.tuple('AUTH_TOKEN_CLASSES'),
    'TOKEN_TYPE_CLAIM': env.str('TOKEN_TYPE_CLAIM'),
    'TOKEN_USER_CLASS': env.str('TOKEN_USER_CLASS'),

    'JTI_CLAIM': env.str('JTI_CLAIM'),

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': env.str('SLIDING_TOKEN_REFRESH_EXP_CLAIM'),
    'SLIDING_TOKEN_LIFETIME': timedelta(
        minutes=env.int('SLIDING_TOKEN_LIFETIME')),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(
        days=env.int('SLIDING_TOKEN_REFRESH_LIFETIME')),
}



