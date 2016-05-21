# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160521_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='description',
            field=models.TextField(default='La Grande Guerre'),
            preserve_default=False,
        ),
    ]
