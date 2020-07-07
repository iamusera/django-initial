from django.db import models
from django.conf import settings
from MyAuth.models import BaseUser
# Create your models here.


class User(models.Model):
    # 创建基础用户
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='用户',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    nickname = models.CharField('昵称', max_length=100, blank=False, unique=True, null=False)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = "文章用户"
        verbose_name_plural = verbose_name


# class Article(models.Model):
#     ...


class ItemBase(models.Model):
    # 多种相同结构表继承自抽象类
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_delete_status = (
        ('0', '未删除'),
        ('1', '删除')
    )
    is_delete = models.CharField(verbose_name='逻辑删除',choices=is_delete_status, max_length=10, default='0')

    def __str__(self):
        return self.owner

    class Meta:
        abstract = True


class Tags(models.Model):
    '''
    文章标签
    '''
    name = models.CharField(max_length=20, verbose_name='tag_name')
    # number = models.IntegerField(default=1, verbose_name='num_tag')
    is_delete_status = (
        ('0', '未删除'),
        ('1', '删除')
    )
    is_delete = models.CharField(verbose_name='逻辑删除',choices=is_delete_status, max_length=10, default='0')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        ordering = ['-id']
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(ItemBase):
    body = models.TextField()
    tags = models.ManyToManyField(Tags, verbose_name=u'blog_tag') # many_to_many 会增加一个中间表

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog'
        ordering = ['-id']
        verbose_name = "文章"
        verbose_name_plural = verbose_name


