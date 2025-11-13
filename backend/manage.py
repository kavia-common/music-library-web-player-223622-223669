#!/usr/bin/env python
import os
import sys

def main():
    """Django's command-line utility for administrative tasks."""
    # Use the unified 'config' project settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
