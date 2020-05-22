from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from ccelery_app.tasks import *
import simplejson
from django.http import HttpResponse


@require_http_methods(["GET"])
def addw(request):
    # c = {'answer': add.delay(1, 2)}
    c = add.delay(1, 2)
    print('view里面',c)
    res = {
        'status':200
    }
    return HttpResponse(status=200, content=simplejson.dumps(res), content_type="application/json,charset=utf-8")

