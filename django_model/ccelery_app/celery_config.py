# celery_config.py

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入指定的任务模块
CELERY_IMPORTS = {
    # 'ccelery_app.tasks',
    'celery_app.tasks',
}
# imports = [
#     "celery_app.tasks",
# ]
