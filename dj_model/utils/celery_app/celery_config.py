# celery_config.py
from celery.schedules import crontab

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入指定的任务模块
CELERY_IMPORTS = {
    # 'celery_app.tasks',
    'tests_.utils.tasks',
    "TestAPP.utils.tasks"
}

CELERYBEAT_SCHEDULE = {
    # 定时任务一：　每5分钟执行一次任务(refresh1)
    'refresh1': {
        "task": "tests_.utils.tasks.heartbeat",
        "schedule": crontab(seconds=2),
        "args": (),
    },
    # # 定时任务二:　每天的凌晨2:00，执行任务(refresh2)
    # 'refresh2': {
    #     "task": "celery_tasks.update_hruser.tasks.refresh",
    #     'schedule': crontab(minute=0, hour=2),
    #     "args": ()
    # },
    # # 定时任务三:每个月的１号的6:00启动，执行任务(refresh3)
    # 'refresh3': {
    #         "task": "celery_tasks.update_hruser.tasks.refresh",
    #         'schedule': crontab(hour=6, minute=0,   day_of_month='1'),
    #         "args": ()
    # },
    }
# CELERY_BEAT_SCHEDULE = {
#     # 'add-every-xx-seconds': {
#     #     'task': 'app_blog.blog.tasks.print_info',
#     #     'schedule': timedelta(seconds=2),  # 每 30 秒一次
#     #     # 'schedule': timedelta(minutes=1),         # 每 1 分钟一次
#     #     # 'schedule': timedelta(hours=4),           # 每 4 小时一次
#     #     'args': ('settings中的定时任务',)  # 任务函数参数，如果只有一个参数，一定要加逗号
#     # },
#     'send_qq_blog_request_count': {
#         'task': 'app_blog.blog.tasks.count_blog_everyday_request',
#         'schedule': crontab(hour=23, minute=30),  # 每天晚上 23 点 30 分执行一次
#     }
# }