# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20160521_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invention',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='invention',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
