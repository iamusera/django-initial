from django.db import models
from django.conf import settings
from MyAuth.models import BaseUser
# Create your models here.


class User(models.Model):
    # 创建权限用户
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='用户',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    nickname = models.CharField('昵称', max_length=100, blank=False, unique=True, null=False)
    class Meta:
        db_table = 'user'
        ordering = ['-id']
        verbose_name = "文章用户"
        verbose_name_plural = verbose_name


# class Article(models.Model):
#     ...


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tags(models.Model):
    '''
    文章标签
    '''
    name = models.CharField(max_length=20,verbose_name='tag_name')
    number = models.IntegerField(default=1, verbose_name='num_tag')


class Blog(ItemBase):
    body = models.TextField()
    tags = models.ManyToManyField(Tags, verbose_name=u'blog_tag')

    class Meta:
        db_table = 'article'
        ordering = ['-id']
        verbose_name = "文章"
        verbose_name_plural = verbose_name


