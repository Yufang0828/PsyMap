# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django.utils.timezone
from django.conf import settings
import django.contrib.postgres.fields.hstore
import django.contrib.postgres.fields.ranges


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('experiment_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('consent_file', models.CharField(max_length=64)),
                ('priority', models.PositiveSmallIntegerField(default=0)),
                ('time_range', django.contrib.postgres.fields.ranges.DateTimeRangeField()),
                ('description', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='QGroup',
            fields=[
                ('qgroup_id', models.AutoField(serialize=False, primary_key=True)),
                ('group_name', models.CharField(max_length=32)),
                ('priority', models.PositiveSmallIntegerField(default=0)),
                ('intro', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='QGroupQuiz',
            fields=[
                ('gq_id', models.AutoField(serialize=False, primary_key=True)),
                ('alias', models.CharField(max_length=64, null=True)),
                ('priority', models.PositiveSmallIntegerField(default=0, null=True)),
                ('intro', models.TextField(default=None, null=True)),
                ('qgroup', models.ForeignKey(to='PsyMap.QGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('screen_name', models.CharField(max_length=128)),
                ('xml_path', models.CharField(max_length=128)),
                ('intro', models.TextField(default=None)),
                ('norm', django.contrib.postgres.fields.hstore.HStoreField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserFillQuiz',
            fields=[
                ('fill_id', models.AutoField(serialize=False, primary_key=True)),
                ('fill_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cost_seconds', models.IntegerField(default=-1)),
                ('ip_addr', models.GenericIPAddressField(default=None, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
                ('answer', django.contrib.postgres.fields.hstore.HStoreField()),
                ('score', django.contrib.postgres.fields.hstore.HStoreField()),
                ('memo', django.contrib.postgres.fields.hstore.HStoreField(default=None, null=True)),
                ('qgroup', models.ForeignKey(to='PsyMap.QGroup')),
                ('quiz', models.ForeignKey(to='PsyMap.Quiz')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLink',
            fields=[
                ('link_id', models.AutoField(serialize=False, primary_key=True)),
                ('site', models.CharField(max_length=8)),
                ('alien', models.CharField(max_length=64)),
                ('token', models.CharField(max_length=256)),
                ('updated', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='qgroupquiz',
            name='quiz',
            field=models.ForeignKey(to='PsyMap.Quiz'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='qgroup',
            field=models.ForeignKey(to='PsyMap.QGroup'),
        ),
    ]
