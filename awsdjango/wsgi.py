"""WSGI entrypoint for AWS deployments."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awsdjango.settings.prod')

application = get_wsgi_application()
