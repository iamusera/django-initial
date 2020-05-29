from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.timezone import now
from django.db import models
import uuid
# Create your views here.


class BaseUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField('昵称', max_length=100, blank=True, unique=True)
    birth_day = models.DateField("生日", blank=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)
    source = models.CharField("创建来源", max_length=100, blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-id']
        verbose_name = "用户"
        verbose_name_plural = verbose_name




class OAuthUser(models.Model):
    fid = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=50, null=True, blank=True)
    nikename = models.CharField(max_length=50, verbose_name='昵称', null=True, blank=True)
    counts = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nikename

    class Meta:
        db_table = 'bg_user'
        verbose_name = 'oauth用户'
        verbose_name_plural = verbose_name


class Article(models.Model):
    fid = models.AutoField(primary_key=True)
    ar_name = models.CharField(max_length=50, null=True, blank=True)
    ar_user = models.ForeignKey(OAuthUser, related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return self.ar_name

    class Meta:
        db_table = 'bg_books'
        verbose_name = '书列表'
        verbose_name_plural = verbose_name

