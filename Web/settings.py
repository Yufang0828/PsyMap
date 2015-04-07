"""
Django settings for Web project.
For more information on this file, see  https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see  https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8d2tfo0#5!(w-62(=pblp6p%&24_^s#^nabwf=#*z_zsn3x90$'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']  # [ 'ccpl.psych.ac.cn', '192.168.', '127.', ]


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'PsyMap',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Web.urls'
WSGI_APPLICATION = 'Web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'PsyMap',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'ccpl_817',
        'OPTIONS': {},
    },
    'lite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'PsyMap',
    }
}

# Internationalization  https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'zh-CN'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'PsyMap/pages/'),
)

# Static files (CSS, JavaScript, Images) https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/PsyMap/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "PsyMap/static/"),
)

USE_X_FORWARDED_HOST = True

from shapely.geometry import Point
from ctypes.util import find_library
GEOS_LIBRARY_PATH = find_library('geos_c')