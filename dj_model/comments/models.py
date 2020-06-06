from django.db import models
from TestApp.models import Article
from django.conf import settings
from django.utils.timezone import now
# Create your models here.


class Comment(models.Model):
    '''
    评论
    '''
    body = models.TextField('正文', max_length=300)
    created_time = models.DateTimeField('create_time', default=now)
    last_mod_time = models.DateTimeField('modify_time', default=now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='author',
        related_name='author',
        on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article,
        verbose_name='blog',
        related_name='article',
        on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self',
        verbose_name="superior_comments",
        related_name='comments',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    is_view = models.BooleanField(
        'is_view', default=True, blank=False, null=False)

    class Meta:
        ordering = ['id']
        verbose_name = "comment"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

