from django.contrib import admin
from TestApp.models import (Article, User, Tags)
# Register your models here.

admin.site.register([Article, User, Tags])
