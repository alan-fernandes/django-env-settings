import os
from pathlib import Path
from shutil import copyfile

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        if not Path('./settings_template.py').exists():
            from django_env_settings import settings_skeleton
            src_path = os.path.abspath(settings_skeleton.__file__)
            copyfile(src_path, './settings_template.py')
            help_txt = '\nA settings_template.py file was created for you to begin with.\n' \
                       'Put all your project environment settings in this file and save\n' \
                       'with your source code, to be used as a template to setup environments.\n'
        else:
            help_txt = '\nA settings_template.py file already exists.'

        print(help_txt)
