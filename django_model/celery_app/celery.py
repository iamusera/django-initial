from __future__ import absolute_import, unicode_literals
from celery import Celery

# from management_web_gowork.settings import PRIVATE_IP

celery_app = Celery("my_celery")

celery_app.config_from_object('celery_app.celery_config')

celery_app.autodiscover_tasks(['celery_app'])