from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path(r"get_token/", views.GetToken.as_view())
]