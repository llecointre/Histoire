# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_usercategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCategory',
        ),
    ]
