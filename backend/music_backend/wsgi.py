import os
from django.core.wsgi import get_wsgi_application

# Redirect to unified config.settings to avoid dual-project confusion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()
