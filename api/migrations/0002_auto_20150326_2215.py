# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='articletag',
            unique_together=set([('article', 'tag')]),
        ),
        migrations.RemoveField(
            model_name='articletag',
            name='count',
        ),
    ]
