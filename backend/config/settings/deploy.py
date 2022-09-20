from pathlib import Path
import os

from .base import *

import environ


def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret

# 환경변수 불러올 수 있도록 세팅
env = environ.Env(DEBUG=(bool, True))

# env 파일의 위치 알려준다.
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l65y8l7w!2g#+%$0f9zo08c9=yu5pr((6*65qz6xzxt+6s&yzt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yoonsu',
        'USER': 'yoonsu',
        'PASSWORD': '1234',
        'HOST': 'yoonsu',
        'PORT': '3306',
    }
}