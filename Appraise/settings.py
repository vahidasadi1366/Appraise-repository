"""
Django settings for Appraise project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import logging
import os
import warnings
from logging.handlers import RotatingFileHandler

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

DEBUG = os.environ.get('APPRAISE_DEBUG', True)
TEMPLATE_DEBUG = os.environ.get('APPRAISE_TEMPLATE_DEBUG', DEBUG)

ADMINS = os.environ.get('APPRAISE_ADMINS', ())
MANAGERS = ADMINS

_SECRET_KEY_DEFAULT = 'j^g&cs_-8-%gwx**xmq64pcm6o2c3ovrxy&%9n@ez#b=qi!uc%'
SECRET_KEY = os.environ.get('APPRAISE_SECRET_KEY', _SECRET_KEY_DEFAULT)
if SECRET_KEY == _SECRET_KEY_DEFAULT:
    warnings.warn(
        'Using the default SECRET_KEY value! Set and export APPRAISE_SECRET_KEY envvar instead'
    )

# ALLOWED_HOSTS = os.environ.get('APPRAISE_ALLOWED_HOSTS', '127.0.0.1').split(',')
ALLOWED_HOSTS = ['*']
WSGI_APPLICATION = os.environ.get(
    'APPRAISE_WSGI_APPLICATION', 'Appraise.wsgi.application'
)

# Try to load database settings, otherwise use defaults.
DB_ENGINE = os.environ.get('APPRAISE_DB_ENGINE')
DB_NAME = os.environ.get('APPRAISE_DB_NAME')
DB_USER = os.environ.get('APPRAISE_DB_USER')
DB_PASSWORD = os.environ.get('APPRAISE_DB_PASSWORD')
DB_HOST = os.environ.get('APPRAISE_DB_HOST')
DB_PORT = os.environ.get('APPRAISE_DB_PORT')

if all((DB_ENGINE, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)):
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {'sslmode': 'require'},
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

FILE_UPLOAD_PERMISSIONS = 0o644

# Logging settings for this Django project.
LOG_LEVEL = logging.DEBUG
LOG_FILENAME = os.path.join(BASE_DIR, 'appraise.log')
LOG_FORMAT = "[%(asctime)s] %(name)s::%(levelname)s %(message)s"
LOG_DATE = "%m/%d/%Y @ %H:%M:%S"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT, LOG_DATE)

# pylint: disable=C0330
LOG_HANDLER = RotatingFileHandler(
    filename=LOG_FILENAME,
    mode="a",
    maxBytes=50 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8",
)
LOG_HANDLER.setFormatter(LOG_FORMATTER)

LOGIN_URL = '/dashboard/sign-in/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Dashboard',
    'EvalView',
    'EvalData',
    'Campaign',
]

if DEBUG:
    try:
        # pylint: disable=W0611
        import debug_toolbar  # type: ignore

        INSTALLED_APPS.append('debug_toolbar')
        warnings.warn('Enabled Django Debug Toolbar in installed apps')
    except ImportError:
        warnings.warn('Django Debug Toolbar not installed')

MIDDLEWARE = []
if DEBUG:
    if 'debug_toolbar' in INSTALLED_APPS:
        MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

MIDDLEWARE.extend(
    [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
)

ROOT_URLCONF = 'Appraise.urls'

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

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# TODO: This is a temporary hack for running Appraise locally for regression
# testing and development as WhiteNoise staticfiles app does not work.
if SECRET_KEY != _SECRET_KEY_DEFAULT:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allow to specify absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.environ.get('APPRAISE_MEDIA_ROOT', '')
if MEDIA_ROOT and MEDIA_ROOT[-1] != '/':
    raise ImproperlyConfigured('MEDIA_ROOT needs to end with a slash!')

# Base context for all views.
BASE_CONTEXT = {
    'commit_tag': '#wmt22dev',
    'title': 'Appraise evaluation system',
    'static_url': STATIC_URL,
}

if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
    ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
