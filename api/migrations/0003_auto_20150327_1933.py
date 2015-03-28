# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150326_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contentUrl',
            field=models.CharField(unique=True, max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gaguser',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='taguser',
            unique_together=set([('user', 'tag')]),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('article', 'user')]),
        ),
    ]
