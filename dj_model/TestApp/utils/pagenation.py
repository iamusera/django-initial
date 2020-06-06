from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict


class MyPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('rows', data)
        ]))
