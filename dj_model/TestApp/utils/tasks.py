from utils.celery_app.celery import celery_app
import time


@celery_app.task
def add(x, y):
    time.sleep(3)
    print('开始异步, test')
    time.sleep(5)
    return x + y


@celery_app.task()
def heartbeat():
    print('i am heart beat...')
    return 1
