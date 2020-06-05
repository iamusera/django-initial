from django.contrib import admin
from TestApp.models import (Blog, User, Tags)
# Register your models here.

admin.site.register([Blog, User, Tags])
