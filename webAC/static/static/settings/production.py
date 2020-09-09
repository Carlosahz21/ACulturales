from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['webac.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'deff1tlhs5es1u',
        'USER': 'xmgsyhrjwaqggf',
        'PASSWORD': 'c64338c2a3169f71669b65802d166d991d3207c683adeb8121b7c7ef8b88dc69',
        'HOST': 'ec2-52-1-95-247.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (BASE_DIR, "static")

