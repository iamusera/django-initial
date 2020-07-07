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
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view  # list_view abandon in 3.10, @action instead
from rest_framework.decorators import action
# 其他
import logging
import json
import mimetypes
from TestApp.utils.filter import ArticleFilter
from TestApp.serializers import *
from TestApp.utils.tasks import *
from collections import OrderedDict
from apscheduler.schedulers.background import BackgroundScheduler

# el
from MyAuth.models import *
from TestApp.utils.pagenation import MyPagination
from utils.PagePangtor import Pagination

# Create your views here.

logger_collect = logging.getLogger(__name__)


class ReturnMsg(object):
    def __init__(self, code=200, msg='succeed', errors=None, data=None):
        self.code = code
        self.msg = msg
        self.errors = {} if errors is None else errors
        self.data = None if data is None else data

    def dict(self):
        return {
            'status': self.code,
            'message': self.msg,
            'data': self.data
        }


class ListViewSet(ModelViewSet):
    def get_queryset(self):
        query = self.queryset
        return query.filter(is_delete='0').order_by('id')

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)
        # May raise a permission denied, NO permission, PLZ!!!
        # self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        res = ReturnMsg(data=response.data).dict()
        return Response(res, status=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict())

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict())

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict())


@csrf_exempt
@require_http_methods(["GET"])
def addw(request):
    c = add.delay(1, 2)
    res = {
        'status': 200
    }
    sess = request.session.items()
    cooki = request.COOKIES['csrftoken']
    return HttpResponse(status=200, content=json.dumps(res), content_type="application/json,charset=utf-8")


class BasicAPIView(APIView):
    queryset = Article.objects.all().order_by('id')

    # 分页和筛选还是使用GenericViewSet方便

    def get(self, request):
        pg = MyPagination()
        pager = pg.paginate_queryset(queryset=self.queryset, request=request, view=self)
        serializer = ArticleSerializer(instance=pager, many=True)
        # return Response(ReturnMsg(data=serializer.data).dict())
        return pg.get_paginated_response(serializer.data)


# @action(methods=['GET', 'POST'], detail=True)
# action(methods=None, detail=None, url_path=None, url_name=None, **kwargs):
# response 请使用HttpResponse/JSONRESPONSE, 不支持DRF的 Response
# detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk>/action方法名/
# True 表示路径格式是xxx/<pk>/action方法名/
# False 表示路径格式是xxx/action方法名/

@action(methods=['GET', 'POST'], detail=True)
def article_list(request):
    return HttpResponse(status=200, content=json.dumps(ReturnMsg(data='ok').dict()),
                        content_type="application/json,charset=utf-8")


class ArticlePage(ListViewSet):
    queryset = Article.objects.all()
    pagination_class = MyPagination
    # filter_class = ArticleFilter
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        logger_collect.info('************** info **************')
        return Response(serializer.data)


@api_view(['POST', 'GET'])
def api_vi(request):
    queryset = Article.objects.all().order_by('id')
    pg = MyPagination()
    pager = pg.paginate_queryset(queryset=queryset, request=request)
    serializer = ArticleSerializer(instance=pager, many=True)
    return pg.get_paginated_response(serializer.data)


def option():
    cursor = connection.cursor()
    cursor.close()
    print('*********************** ok ***************************')


sched = BackgroundScheduler()
sched.add_job(option, 'interval', seconds=10, id='option')
sched.start()
print(sched.get_jobs())
