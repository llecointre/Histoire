# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Personnage',
            new_name='Character',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='subcategories',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='nom',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
