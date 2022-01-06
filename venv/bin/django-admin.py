#!/Users/apple/Desktop/github/praktikum/sprint_3/yatube_project/venv/bin/python3
<<<<<<< HEAD
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
=======
from django.core import management

if __name__ == "__main__":
>>>>>>> 0efae6b8ba0995009ac8fdaa5b7c1f9fa1ac2988
    management.execute_from_command_line()
