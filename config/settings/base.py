"""
Django settings for bluejobs project.
"""

from pathlib import Path

from django.contrib.messages import constants as messages
from django.urls import reverse_lazy

import dj_database_url
from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config(
    'SECRET_KEY', default='django-insecure$config.settings.local')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*'] # config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',

    'apps.accounts',
    'apps.core',
    'apps.jobs',
    # 'apps.blog',

    'crispy_forms',
    'crispy_bootstrap5',
    'django_cleanup.apps.CleanupConfig',
    'widget_tweaks',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'config.urls'

INTERNAL_IPS = ['127.0.0.1']

WSGI_APPLICATION = 'config.wsgi.application'

SITE_ID = 1


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.accounts.middleware.UpdateLastSeenMiddleware',
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.parent / 'templates'],
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


# ==============================================================================
# DATABASES SETTINGS
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
    # 'default': dj_database_url.config(
    #     default=config(
    #         'DATABASE_URL', default='postgres://simple:simple@localhost:5432/bluejobs_db'),
    #     conn_max_age=600,
    # )
}

# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
#         'NAME': config('DB_NAME', BASE_DIR.parent / 'db.sqlite3'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST', 'localhost'),
#         'PORT': config('DB_PORT', 5432),
#     }
# }


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
# ==============================================================================

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

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


# ==============================================================================
# I18N AND L10N SETTINGS
# https://docs.djangoproject.com/en/4.0/topics/i18n/
# ==============================================================================

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR.parent / 'locale'
]


# ==============================================================================
# STATIC FILES SETTINGS
# https://docs.djangoproject.com/en/4.0/howto/static-files/
# ==============================================================================

STATIC_URL = '/static/'

# BASE_DIR.parent.parent / "static"
STATIC_ROOT = BASE_DIR.parent / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR.parent / 'static',
]

# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.parent / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


# ABSOLUTE_URL_OVERRIDES = {
#     'auth.user': lambda u: reverse_lazy('resume_detail', args=[u.username])
# }

# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'


# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

LOGOUT_REDIRECT_URL = 'core:home'

LOGIN_REDIRECT_URL = 'core:dashboard'

LOGIN_URL = 'auth:login'

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "apps.accounts.backends.EmailAuthenticationBackend",
]

AUTH_USER_MODEL = 'accounts.User'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'your_account@gmail.com'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# EMAIL_PORT = config('EMAIL_PORT', cast=int)
PROJECT_ENVIRONMENT = config("PROJECT_ENVIRONMENT", default="local")
