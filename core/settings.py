
from pathlib import Path
from os.path import join
import os
import environ

env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG"))

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.products.apps.ProductsConfig',
    'apps.cart.apps.CartConfig',
    'apps.orders.apps.OrderConfig',
    'apps.administration.apps.AdministrationConfig'
]

THIRD_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'simple_history',
    'django_filters',
    'django_rest_passwordreset',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

TOKEN_EXPIRED_AFTER_SECONDS = 10

# Middlewares Settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'core.urls'

# Templates Settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, "apps/administration/templates")
        ],
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
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("NAME_DATABASE"),
        'USER': os.environ.get("USER_DATABASE"),
        'PASSWORD': os.environ.get("PASSWORD_DATABASE"),
        'HOST': os.environ.get("HOST_DATABASE"),
        'PORT': os.environ.get("PORT_DATABASE")
    }
}

DATABASES = MYSQL


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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = join(BASE_DIR, 'staticfiles/')

STATICFILES_DIRS = [
    join(BASE_DIR, 'apps/administration/static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media Files Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media/')

# Urls Redirect Login
LOGIN_REDIRECT_URL = '/administration/dashboard/'

LOGOUT_REDIRECT_URL = '/administration/auth/login/'

LOGIN_URL = '/administration/auth/login/'

# Rest Framwwork Settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser'
    ],
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata'
}

AUTH_USER_MODEL = 'users.User'

# LOGIN_REDIRECT_URL = '/'

# Urls allowed
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = ['DELETE','GET','OPTIONS','POST','PUT']

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with'
]

# Settings send email for django
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    DEFAULT_FROM_EMAIL = 'Garden Store - Store Shopping Academia <mail@gmail.com>'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))
    EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS"))
    EMAIL_USE_SSL = bool(os.environ.get("EMAIL_USE_SSL"))
