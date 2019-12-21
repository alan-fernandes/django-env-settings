Django Environment Settings
===========================

This simple project make easy to have separate settings for different environments,
and to inform which environment is active by creating a file whith the environment
name in the source folder.

Installation
------------

    pip install git+https://github.com/gustavo80br/django-env-settings.git

Usage
-----

Add 'django_env_settings' to the project to your INSTALLED_APPS.
    
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_env_settings',
]
```

Add this line to the end of your Django settings.py file:

```python
from django_env_settings import *
```

Create a proto settings_skeleton.py file. This file will be generated at the same level as manage.py. Edit this file
content and copy to this file the variables you want to override for specific environments. This file will be the
template for your environment defined settings file.

Use this command to create the skeleton file:

    python manage.py create_django_env_template_file

After creating the settings_skeleton.py file, run the command:

    python manage.py create_django_env_files

Now you will find in you source root folder the following files:

- settings_dev.py
- settings_staging.py
- settings_production.py

Edit this file with the specific settings for each environment, and define which one is in use by creating one of the
following files in the source root folder:

    __dev__.py
    __staging__.py
    __production__.py

Now the settings variable will be used from the respective settings file and will be easier for you to control this
kind of configuration in your GIT repository.

Have fun!
