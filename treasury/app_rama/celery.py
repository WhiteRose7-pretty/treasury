import os
from celery import Celery
from django.conf import settings

__author__ = ""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_rama.settings')

app = Celery('app_rama')

CELERY_TIMEZONE = 'IST'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
