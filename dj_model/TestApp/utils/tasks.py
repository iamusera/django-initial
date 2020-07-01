from celery_app.celery import celery_app
import time
import os
from django.db import connection
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@celery_app.task
def add(x, y):
    time.sleep(3)
    print('开始异步, test')
    time.sleep(5)
    return x + y


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'dj_model.settings')


@celery_app.task()
def heartbeat():
    # cursor = connection.cursor
    # cursor.close()
    # bug, django.db.utils.DatabaseError: DatabaseWrapper objects created in a thread can only be used in that same
    # thread. The object with alias 'default' was created in thread
    # id 2132849328376 and this is thread id 2132857750984.
    logger.info(msg='****************************** i am heart beat... ******************************')
