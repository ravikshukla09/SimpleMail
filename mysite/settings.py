"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '14s607==c2(l(7j9&z^%c6fj_61f)v4_n-r)7dzf7+6j91hyo1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['simple-mail.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'email_service',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ADMINS = [('Ravi', 'ravikshukla09@gmail.com')]
EMAIL_SUBJECT_PREFIX = "[Django] - Ravi: "
# SERVER_EMAIL = 'ravikshukla09@gmail.com'

import dj_database_url
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)