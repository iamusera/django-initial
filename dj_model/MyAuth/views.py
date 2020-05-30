# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings
import jwt
import time
from django.db import connection
# Create your views here.


class GetToken(APIView):
    authentication_classes = []

    def get(self, request):
        user_id = request.GET.get('user_id')
        dic = {
            'exp': int(time.time()) + 60*10,
            'data': {
                'user_name': user_id,
            },
        }
        ai_token = jwt.encode(dic, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        key = "_".join(['Token', user_id])
        cache.set(key, ai_token, 60*60)
        return Response(status=200, data={'ai_token': ai_token})
