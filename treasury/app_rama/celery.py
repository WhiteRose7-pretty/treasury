import os
from celery import Celery
from django.conf import settings


# set the default Django modulus for celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_rama.settings')

app = Celery('app_rama')  # @@@ optionally you can change app_rama to app here

app.config_from_object('django.conf:settings')  # @@@ optionally you can pass the name space

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
