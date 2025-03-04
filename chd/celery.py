import os

from django.conf import settings
from celery import Celery

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chd.settings")

app = Celery("chd")

# Load task modules from all registered Django apps
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.result_key_prefix = settings.DB_PREFIX

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()
