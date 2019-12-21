
# ------------------------------------------------------------------
# Determine environment based on __env__ file on project source root
# ------------------------------------------------------------------

import os
from pathlib import Path
from shutil import copyfile


def get_environment():
    try:
        import __dev__
        return 'dev'
    except ImportError:
        try:
            import __staging__
            return 'staging'
        except ImportError:
            try:
                import __production__
                return 'production'
            except ImportError:
                return None


ACTUAL_ENV = get_environment()
if ACTUAL_ENV:
    try:
        if ACTUAL_ENV == 'dev':
            from settings_dev import *
        elif ACTUAL_ENV == 'staging':
            from settings_staging import *
        elif ACTUAL_ENV == 'production':
            from settings_production import *
    except ImportError:
        help_txt = ''
        if not Path('./settings_template.py').exists():
            import django_env_settings.settings_skeleton
            src_path = os.path.abspath(settings_skeleton.__file__)
            copyfile(src_path, './settings_template.py')
            help_txt = '\nA settings_template.py file was created for you to begin with.\n' \
                       'Put all your project environment settings in this file and save\n' \
                       'with your source code, to be used as a template to setup environments.\n'
        raise SystemError('\n\nFile settings_{env}.py not found in source code root.\n'
                          '---------------------------------------------------------------------\n'
                          'Your environment is set as {env}, but no settings_{env}.py was found.\n'
                          'Create a settings_{env}.py file to hold your environment specific settings.\n'
                          'Save the file in your source code root.\n'
                          '{help_txt}'.format(env=ACTUAL_ENV, help_txt=help_txt))

else:
    raise SystemError('\n\nNo Environment set!\n'
                      '-------------------\n'
                      'Please, determine in which environment the code is running,\n'
                      'by creating the respective environment file in your source code root.\n'
                      'The options are:\n\n'
                      '  __dev__.py\n'
                      '  __staging__.py\n'
                      '  __production__.py\n')

