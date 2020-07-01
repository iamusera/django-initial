daphne dj_model.asgi:application;
celery -A celery_app worker -l debug -P eventlet -f logs/celery.log;
celery beat -A celery_app -l info;
echo "启动成功"
