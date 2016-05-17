# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='period',
            old_name='nom',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='nom',
            new_name='name',
        ),
    ]
