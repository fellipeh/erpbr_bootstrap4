# -*- coding: utf-8 -*-
import os
import sys
import tempfile

from decouple import config as decouple_config, Csv
from dj_database_url import parse as dburl

from django.utils.translation import ugettext_lazy as _
import settings_local

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.dirname(SETTINGS_DIR)

PROJECT_VERSION = decouple_config('PROJECT_VERSION', default='version_not_defined')

SECRET_KEY = decouple_config('SECRET_KEY', default='efhrIG103A476erwcEL1Keko69fmV9W7sCZluX')

DEBUG = decouple_config('DEBUG', default=False)
TEST = decouple_config('TEST', default=False)

ALLOWED_HOSTS = decouple_config('ALLOWED_HOSTS', default='localhost, 127.0.0.1', cast=Csv())

ADMINS = (
    ('Fellipe', 'fellipeh@gmail.com'),
)

MANAGERS = (ADMINS[0],)

# Application definition
SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'publico.apps.PublicoConfig',  # you must list the app where your tenant model resides in
    'django.contrib.contenttypes',

    # everything below here is optional
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',

    # your tenant-specific apps
    # 3rd apps
    'widget_tweaks',
    'bootstrap4',
    'crispy_forms',
    'password_reset',
    'rest_framework',

    # ERPbr apps
    'account.apps.AccountConfig',
    # 'api.apps.ApiConfig',
    'core.apps.CoreConfig',
    'desk.apps.DeskConfig',
    'cadastro.apps.CadastroConfig',
    # 'financeiro.apps.FinanceiroConfig',
    # 'estoque.apps.EstoqueConfig'
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_tools.middlewares.ThreadLocal.ThreadLocalMiddleware',
]

ROOT_URLCONF = 'erpbr.urls'
PUBLIC_SCHEMA_URLCONF = 'erpbr.urls_public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'erpbr.context_processor.default_proc',
            ],
        },
    },
]

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

TENANT_MODEL = "publico.ErpBrClient"

WSGI_APPLICATION = 'erpbr.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = settings_local.DATABASES

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'account.CustomUser'

LOGIN_URL = 'account:erpbr_login'

LOGIN_REDIRECT_URL = 'desk:dashboard'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') if not TEST else tempfile.mkdtemp()

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# when run collectstatic the result will be here
STATIC_ROOT = os.path.join(BASE_DIR, 'static_deploy')

ADMIN_MEDIA_PREFIX = '/static/admin/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = False
CRISPY_CLASS_CONVERTERS = {'textinput': "input-sm"}

BOOTSTRAP4 = {
    'form_error_class': 'bootstrap4-error',
    'form_required_class': 'bootstrap4-required',
    'include_jquery': False,
}

EMAIL_USE_TLS = True
EMAIL_HOST = decouple_config('EMAIL_HOST', default='')
EMAIL_PORT = decouple_config('EMAIL_PORT', default='')
EMAIL_HOST_USER = decouple_config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = decouple_config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = decouple_config('DEFAULT_FROM_EMAIL', default='')

LOG_DIR = decouple_config('LOG_DIR', default=os.path.join(BASE_DIR, 'log'))

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(pathname)s:%(funcName)s:%(lineno)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'erpbr.log'),
            'maxBytes': 1024 * 1024 * 15,
            'backupCount': 5,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'core': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'account': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
        }
    }
}

try:
    from settings_local import *
except ImportError:
    pass
