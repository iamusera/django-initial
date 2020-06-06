import django_filters
from TestApp.models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = Article
        fields = '__all__'