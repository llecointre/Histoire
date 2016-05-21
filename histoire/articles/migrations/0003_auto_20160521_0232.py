# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('network', '0006_delete_usercategory'),
        ('articles', '0002_auto_20160517_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ArtArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('art', models.ForeignKey(to='articles.Art')),
                ('author', models.ManyToManyField(to='network.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('marker', models.OneToOneField(to='map.Marker')),
            ],
        ),
        migrations.CreateModel(
            name='BattleArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('battle', models.ForeignKey(to='articles.Battle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('marker', models.OneToOneField(to='map.Marker')),
            ],
        ),
        migrations.CreateModel(
            name='InventionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('invention', models.ForeignKey(to='articles.Invention')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PeopleArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PeriodArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Philosophy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhilosophyArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('philosophy', models.ForeignKey(to='articles.Philosophy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReligionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('religion', models.ForeignKey(to='articles.Religion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='War',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WarArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('invention', models.ForeignKey(to='articles.Invention')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='marker',
            field=models.OneToOneField(default=1, to='map.Marker'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='period',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='regionarticle',
            name='region',
            field=models.ForeignKey(to='articles.Region'),
        ),
        migrations.AddField(
            model_name='periodarticle',
            name='period',
            field=models.ForeignKey(to='articles.Period'),
        ),
        migrations.AddField(
            model_name='peoplearticle',
            name='people',
            field=models.ForeignKey(to='articles.People'),
        ),
        migrations.AddField(
            model_name='characterarticle',
            name='character',
            field=models.ForeignKey(to='articles.Character'),
        ),
        migrations.AddField(
            model_name='battle',
            name='war',
            field=models.ForeignKey(to='articles.War'),
        ),
    ]
