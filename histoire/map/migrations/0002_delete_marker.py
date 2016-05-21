# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20160521_0332'),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Marker',
        ),
    ]
