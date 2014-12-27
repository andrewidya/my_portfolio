"""
Django settings for my_portfolio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SERVER_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

SITE_ID = '1'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y2coq%lk86_k&ta!twuus&#p2f%2mk(yynw@9@%ax7j0sxyzh3'

# SECURITY WARNING: don't run with debug turned on in production!

#if not os.environ.get("HOME") == '/home/andre':
#   DEBUG = False
#else:
#    DEBUG = True

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['https://andrewidya-portfolio.herokuapp.com']

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

# Application definition

INSTALLED_APPS = (
    #'suit',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'mptt',
    'content',
    'pages',
    'gallery',
    'userprofile',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'my_portfolio.urls'

WSGI_APPLICATION = 'my_portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'andrewidya-portfolio',
        'USER': 'andre',
        'PASSWORD': 'andre',
        'HOST': ''
    }

    #
    # HEROKU configuration
    #
    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'dec942crsm5l7s',
    #    'USER': 'yeavwhhszhgnko',
    #    'PASSWORD': 'X6l1meJuCT9xlAnciydgPXRlE9',
    #    'HOST': 'ec2-54-235-99-22.compute-1.amazonaws.com'
    #}
}

if not os.environ.get("HOME") == '/home/andre':
    # Parse database configuration from $DATABASE_URL
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
        os.path.join(SERVER_BASE_DIR, 'static'),
    )
MEDIA_ROOT = os.path.join(SERVER_BASE_DIR, 'media/')
MEDIA_URL = 'http://127.0.0.1:8000/media/'
SYSTEM_THEMES = ''



# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'