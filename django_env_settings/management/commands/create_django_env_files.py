import os
from pathlib import Path
from shutil import copyfile

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        files = [
            'settings_dev',
            'settings_staging',
            'settings_production'
        ]

        help_text = []

        try:
            import settings_template
        except ImportError:
            print('Could not find settings_template file! Run manage.py create_django_env_temmplate_file to create one')
            return

        for f in files:
            if not Path(f'./{f}.py').exists():
                src_path = os.path.abspath(settings_template.__file__)
                copyfile(src_path, f'./{f}.py')
                help_text.append(f'A {f}.py file was created for you to begin with.')
            else:
                help_text.append(f'A {f}.py file already exists.')

        print('\n'.join(help_text))
