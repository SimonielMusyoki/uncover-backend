import os
from datetime import timedelta
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(hptd!)t@_7l-=f%(**&8m3rju-gpj3kzozt%l##xxjo-sh$4t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 0

ALLOWED_HOSTS = ['*']


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'djoser',
    'ckeditor',
    "debug_toolbar",
    "corsheaders"
]

PROJECT_APPS = [
    "apps.accounts",
    "apps.store",
    "apps.orders",
    "apps.content"
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = str(BASE_DIR / "mediafiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "accounts.User"

# Responsible for sending automated emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587',
EMAIL_USE_TLS =  True

# if PRODUCTION:
#     EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
#     EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
# else:
#     env = environ.Env()
#     environ.Env.read_env()
#     EMAIL_HOST_USER = env("EMAIL_HOST_USER")
#     EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
ACCOUNT_SERIALIZER = 'apps.accounts.serializers.UserCreateSerializer'
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}
DOMAIN = ("localhost:8081")  # local: localhost:3000
SITE_NAME = ('Uncover Skincare')
DEFAULT_FROM_EMAIL = "info@uncoverskincare.co"
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': ACCOUNT_SERIALIZER,
        'user': ACCOUNT_SERIALIZER,
        'current_user': ACCOUNT_SERIALIZER,
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
