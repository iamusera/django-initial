from django.http import HttpResponse
from rest_framework.response import Response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.db import connection

# DRF
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import list_route  # abandon in 3.10, @action instead
from rest_framework.decorators import action
# 其他
import logging
import json
import mimetypes
from TestApp.utils.tasks import *
from collections import OrderedDict

# el
from MyAuth.models import *
from TestApp.utils.pagenation import MyPagination

# Create your views here.

logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["GET"])
def addw(request):
    c = add.delay(1, 2)
    print('view里面', c)
    res = {
        'status': 200
    }
    # session
    sess = request.session.items()
    # cookie
    cooki = request.COOKIES['csrftoken']
    return HttpResponse(status=200, content=json.dumps(res), content_type="application/json,charset=utf-8")


class BasicAPIView(APIView):
    ...


class BasicGenericView(ModelViewSet):
    ...

# @action(methods=['GET', 'POST'], detail=True)
# detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk>/action方法名/
# True 表示路径格式是xxx/<pk>/action方法名/
# False 表示路径格式是xxx/action方法名/
