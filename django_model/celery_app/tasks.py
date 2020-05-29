from .celery import celery_app
import time


@celery_app.task
def add(x, y):
    time.sleep(3)
    print('开始异步')
    time.sleep(5)
    return x + y
