#
# Example of settings_[env].py file
#
# Customize this file as you need
#
# Create a settings_dev.py file for development settings
# Create a settings_staging.py for staging settings
# Create a settings_production.py for production settings
#
# To select which settings to use, create a file called __[env]__.py
#
#   __dev__.py -> Development environment, will use settings_dev.py
#   __staging__.py -> Staging environment, will use settings_stating.py
#   __production__.py -> Production environment, will use settings_production.py
#
# In the last line of the settings.py file, import django_env_settings, like this:
#
#   >> from django_env_settings import *
#
# Have fun!
#

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2b5k05k-!x6+tfeqf-8(y#zi)^a=cd28io#rc6gs2%gnylta8g'

# Environment Allowed Hosts
ALLOWED_HOSTS = ['*']

# Environment Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gemserver',
        'USER': 'gemserver',
        'PASSWORD': 'pass;123',
        'HOST': '192.168.32.51',
        'PORT': '5432',
    },
}

# Add any other settings.py variable below this line, will override the default value in settings.py