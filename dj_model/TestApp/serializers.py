from rest_framework import serializers
from TestApp.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField(required=False)
    created = serializers.SerializerMethodField(required=False)
    updated = serializers.SerializerMethodField(required=False)
    is_delete = serializers.SerializerMethodField(required=False)

    def get_tags(self, obj):
        tags = obj.tags.all().values_list('name', flat=True)
        return tags

    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')

    def get_updated(self, obj):
        return obj.updated.strftime('%Y-%m-%d %H:%M:%S')

    def get_is_delete(self, obj):
        return obj.get_is_delete_display()

    class Meta:
        model = Article
        fields = '__all__'
