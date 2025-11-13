import os
from django.core.asgi import get_asgi_application

# Redirect to unified config.settings to avoid dual-project confusion
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_asgi_application()
