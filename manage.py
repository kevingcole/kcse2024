# manage.py

#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'it_asset_system.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Django is not installed, please install it before proceeding."
            )
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()