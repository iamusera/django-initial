# Generated by Django 3.0.5 on 2020-06-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='昵称'),
        ),
    ]
