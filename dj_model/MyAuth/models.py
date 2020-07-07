from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.timezone import now
from django.db import models
import uuid


# Create your views here.


class BaseUser(AbstractUser):
    # 需要重写manager
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField('昵称', max_length=100, blank=True, unique=True)
    birth_day = models.DateField("生日", blank=True, null=True)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)
    source = models.CharField("创建来源", max_length=100, blank=True, null=True)
    is_delete_status = (
        ('0', '未删除'),
        ('1', '删除')
    )
    is_delete = models.CharField(verbose_name='逻辑删除', choices=is_delete_status, max_length=10, default='0')

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-id']
        verbose_name = "用户"
        verbose_name_plural = verbose_name
