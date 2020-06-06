from django.urls import path, re_path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
# router.register(r'add', views.addw, base_name='add')
# routes.register("user", UserView)   @listview
urlpatterns = [
    path(r"add/", views.addw),  # DRF不能注册函数型视图

]
urlpatterns += router.urls

# router = routers.SimpleRouter()
# router.register(r'add', views.addw, base_name='add')
# 注册的2种方式
# 1. urlpatterns += router.urls
# 2. urlpatterns = [
#     ...
#     url(r'^', include(router.urls))
# ]
