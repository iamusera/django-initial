from django.http import HttpResponse
from rest_framework.response import Response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.db import connection

# DRF
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# 其他
import mimetypes
import simplejson
from celery_app.tasks import *
from collections import OrderedDict

# el
from Myauth.models import *
# Create your views here.


@csrf_exempt
@require_http_methods(["GET"])
def addw(request):
    c = add.delay(1, 2)
    print('view里面',c)
    res = {
        'status':200
    }
    # session
    sess = request.session.items()
    # cookie
    cooki = request.COOKIES['csrftoken']
    print(cooki)
    return HttpResponse(status=200, content=simplejson.dumps(res), content_type="application/json,charset=utf-8")


class BasicView(APIView):
    ...