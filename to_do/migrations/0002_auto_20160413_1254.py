# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_list',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='description',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
