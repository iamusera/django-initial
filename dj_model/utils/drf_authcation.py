from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import (AuthenticationFailed, APIException)
from django.core.cache import cache


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        ai_token = request.COOKIES.get('Ai-Token')
        user_id = request.COOKIES.get('user_id')
        if not ai_token:
            raise AuthenticationFailed({"msg":"无效的token", "code":403, "data":None})
        key = "_".join(['Token', user_id])
        cache_token = cache.get(key)
        if ai_token == cache_token:
            pass
        else:
            raise AuthenticationFailed({"msg":"无效的token", "code":403, "data":None})

    def authenticate_header(self, request):
        pass
