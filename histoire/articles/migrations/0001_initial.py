# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ArtArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('description', models.TextField()),
                ('beginDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BattleArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
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
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('character', models.ForeignKey(to='articles.Character')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
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
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('people', models.ForeignKey(to='articles.People')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('period', models.ForeignKey(to='articles.Period')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Philosophy',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PhilosophyArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
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
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('region', models.ForeignKey(to='articles.Region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReligionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('beginDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WarArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='Date de parution', auto_now_add=True)),
                ('content', models.TextField()),
                ('nb_views', models.IntegerField(default=0)),
                ('author', models.ManyToManyField(to='network.Profil')),
                ('war', models.ForeignKey(to='articles.War')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='battle',
            name='war',
            field=models.ForeignKey(to='articles.War'),
        ),
    ]
