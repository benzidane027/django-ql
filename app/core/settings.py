"""
Django settings for django project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os
from typing import List, Tuple
from decouple import config as ENV

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#AUTH_PROFILE_MODULE = 'accounts.UserProfile'
AUTH_USER_MODEL = "accounts.profile"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  ENV("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production! 
DEBUG =  bool(ENV("DEBUG"))

ALLOWED_HOSTS =  ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://127.0.0.1',
    'https://15.0.0.30',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    'http://127.0.0.0:8000',
    'https://127.0.0.0',
    'https://15.0.0.30'
]
CSRF_TRUSTED_ORIGINS = ["https://localhost","https://127.0.0.1",'https://15.0.0.30']
# Application definition
INSTALLED_APPS = [
    # my apps
    'accounts',
    'graph',
    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    #'rest_framework.authtoken',
    'djoser',
    'imagekit',
    'corsheaders',
    'graphene_django',
    'minio_storage',

    
    
]

MIDDLEWARE = [
    
    #Threed party    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    #core
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DJOSER = {
    # 'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    # 'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    # 'ACTIVATION_URL': '#/activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL': True,
    "LOGIN_FIELD": "email",
    'SERIALIZERS': {
        'user': 'accounts.serializers.UserSerializer',
        'user_create':'accounts.serializers.createUserSerializer',
        'current_user':'accounts.serializers.currentUserSerializer',
        'user_delete':'accounts.serializers.deleteUserSerializer'
        },
}
GRAPHENE = {
    "SCHEMA": "graph.schema.schema"
}


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": ENV("POSTGRES_DB"),
        "USER": ENV("POSTGRES_USER"),
        "PASSWORD": ENV("POSTGRES_PASSWORD"),
        "HOST": ENV("POSTGRES_HOST"),
        "PORT": ENV("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.TokenAuthentication',  # this class can't hand time expiration
        #"accounts.authentication.ExpiringTokenAuthentication", # this class can hand time expiration
        #'rest_framework.throttling.UserRateThrottle'           # define request call number for api
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

#AUTH_TOKEN_VALIDITY = timedelta(days=60)

SIMPLE_JWT = {
'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
'REFRESH_TOKEN_LIFETIME': timedelta(minutes=360),
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#### MINIO

DEFAULT_FILE_STORAGE     = ENV("DEFAULT_FILE_STORAGE")
MINIO_STORAGE_USE_HTTPS  = False
MINIO_STORAGE_ENDPOINT   = f"{ENV("MINIO_ENDPOINT_URL")}:{ENV("MINIO_ENDPOINT_PORT")}"
MINIO_STORAGE_ACCESS_KEY = ENV("MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = ENV("MINIO_STORAGE_SECRET_KEY")
MINIO_STORAGE_MEDIA_BUCKET_NAME = ENV("MINIO_STORAGE_MEDIA_BUCKET_NAME")


