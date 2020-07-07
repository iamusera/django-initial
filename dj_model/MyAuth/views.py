# from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect    # 前后端不分离，重定向到页面用的多
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings
import jwt
import time
from django.db import connection
# Create your views here.


class Login(APIView):
    def get(self, request):
        return Response('redirect')

    def post(self, request):
        name = request.data.get("name")
        pw = request.data.get("pw")

        # user_id = request.GET.get('user_id')
        dic = {
            'exp': int(time.time()) + 60*10,
            'data': {
                'user_name': name,
            },
        }
        my_token = jwt.encode(dic, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        key = "_".join(['Token', name])
        cache.set(key, my_token, 60*60)
        return Response(status=200, data={'my_token': my_token})


class Register(APIView):
    def post(self, request):
        return redirect(reverse('login'))
