from django.db import models
# Create your views here.


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

