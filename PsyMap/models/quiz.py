# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.db.models import *
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import DateTimeRangeField, HStoreField

from django.contrib.auth.models import User


class Quiz(Model):
    __slots__ = ['quiz_id', 'screen_name', 'xml_path', 'intro']
    quiz_id = CharField(max_length=64, primary_key=True)
    screen_name = CharField(max_length=128)
    xml_path = CharField(max_length=128)
    intro = TextField(default=None)


class QGroup(Model):
    __slots__ = ['qgroup_id', 'group_name', 'priority', 'intro']
    qgroup_id = AutoField(primary_key=True)
    group_name = CharField(max_length=32)
    priority = PositiveSmallIntegerField(default=0)
    intro = TextField(default=None)


class QGroupQuiz(Model):
    __slots__ = ['gq_id', 'qgroup', 'quiz', 'alias', 'priority', 'intro']
    gq_id = AutoField(primary_key=True)
    qgroup = ForeignKey(QGroup)
    quiz = ForeignKey(Quiz)
    alias = CharField(max_length=64)
    priority = PositiveSmallIntegerField(default=0)
    intro = TextField(default=None)


class Experiment(Model):
    __slots__ = ['experiment_id', 'name', 'qgroup', 'consent_file', 'priority', 'time_range', 'description']
    experiment_id = AutoField(primary_key=True)
    name = CharField(max_length=64)
    qgroup = ForeignKey(QGroup)
    consent_file = CharField(max_length=64)
    priority = PositiveSmallIntegerField(default=0)
    time_range = DateTimeRangeField()
    description = TextField(default=None)


class UserFillQuiz(Model):
    __slots__ = ['fill_id', 'user', 'quiz', 'qgroup', 'fill_time', 'cost_seconds', 'ip_addr', 'location', 'answer', 'score', 'memo']
    fill_id = AutoField(primary_key=True)
    user = ForeignKey(User)
    quiz = ForeignKey(Quiz)
    qgroup = ForeignKey(QGroup)
    fill_time = DateTimeField(auto_now=True)
    cost_seconds = PositiveSmallIntegerField()
    ip_addr = GenericIPAddressField(default=None)
    location = PointField(null=True)
    answer = HStoreField()
    score = HStoreField()
    memo = HStoreField(default=None)