# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20160417_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='network.Profil', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='network.Category', default=1),
            preserve_default=False,
        ),
    ]
