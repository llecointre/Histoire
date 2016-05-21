# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20160521_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battle',
            name='marker',
        ),
        migrations.RemoveField(
            model_name='character',
            name='marker',
        ),
        migrations.RemoveField(
            model_name='invention',
            name='marker',
        ),
        migrations.AddField(
            model_name='battle',
            name='latitude',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='battle',
            name='longitude',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='character',
            name='latitude',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='character',
            name='longitude',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='invention',
            name='latitude',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AddField(
            model_name='invention',
            name='longitude',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='battle',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='invention',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
