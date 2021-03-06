# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

import json
from collections import defaultdict, namedtuple

from django.db.models import *
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import DateTimeRangeField, HStoreField
from jsonfield import JSONField
from django.db import connection
from django.utils import timezone
from django.contrib.auth.models import User

from quizlite.questionnaire import QService


hstore_to_dict = lambda hstr: json.loads('{%s}' % hstr.replace('=>', ':'))
dict_to_hstore = lambda dic: json.dumps(dic).replace(':', '=>').strip('{ }')

Norm = namedtuple('Norm', 'label, count, avg, min, max, std')


class Quiz(Model):
    __slots__ = ['quiz_id', 'screen_name', 'xml_path', 'intro', 'norm']
    quiz_id = CharField(max_length=64, primary_key=True)
    screen_name = CharField(max_length=128)
    xml_path = CharField(max_length=128)
    intro = TextField(default=None)
    norm = JSONField(default=None, null=True)  # 存储常模, load_kwargs={'object_pairs_hook': OrderedDict}

    def __unicode__(self):
        return '%s [%s]' % (self.quiz_id, self.screen_name)

    def get_questionnaire(self):
        try:
            return QService.get_questionnaire(self.xml_path, quiz_id=self.quiz_id)
        finally:
            QService.set_norm(self.quiz_id, self.get_norm())

    def get_norm(self):
        if self.norm is None:
            self.update_score()
            self.update_norm()
        return self.norm

    def update_score(self):
        fills = UserFillQuiz.objects.raw(
            'SELECT fill_id, answer::JSON, score::JSON FROM "PsyMap_userfillquiz" WHERE quiz_id=%s', (self.quiz_id,)
        )
        cursor = connection.cursor()
        quiz = QService.get_questionnaire(self.xml_path, quiz_id=self.quiz_id)
        for f in fills:
            score = quiz.score(f.answer)
            score = dict_to_hstore(dict(score))  # convert json string to hstore string
            cursor.execute('UPDATE "PsyMap_userfillquiz" SET score=%s::HSTORE WHERE fill_id=%s', (score, f.fill_id))

    def update_norm(self):
        fills = UserFillQuiz.objects.raw(
            'SELECT fill_id, score::JSON FROM "PsyMap_userfillquiz" WHERE quiz_id=%s', (self.quiz_id,)
        )
        counter, avg = defaultdict(int), defaultdict(float)
        _min, _max, std = defaultdict(float), defaultdict(float), defaultdict(float)
        for f in fills:
            for dim, score in f.score.iteritems():
                counter[dim] += 1
                score = float(score)
                avg[dim] += score
                std[dim] += score ** 2
                if score > _max[dim]:
                    _max[dim] = score
                if score < _min[dim]:
                    _min[dim] = score

        self.norm = {}
        # Norm : 'name, count, avg, min, max, std'
        quiz = self.get_questionnaire()
        for dim, average in avg.iteritems():
            try:
                tag = quiz.tags.get(dim).label
            except:
                tag = self.screen_name
            n = counter[dim]
            average /= n
            std[dim] = (std[dim]/n - average**2)**0.5
            self.norm[dim] = Norm(tag, n, average, _min[dim], _max[dim], std[dim]).__dict__

        cursor = connection.cursor()
        norm = json.dumps(self.norm, ensure_ascii=False, sort_keys=True, indent=4)
        cursor.execute('UPDATE "PsyMap_quiz" SET norm=%s::JSONB WHERE quiz_id=%s', (norm, self.quiz_id))


class QGroup(Model):
    __slots__ = ['qgroup_id', 'group_name', 'priority', 'intro']
    qgroup_id = AutoField(primary_key=True)
    group_name = CharField(max_length=32)
    priority = PositiveSmallIntegerField(default=0)
    intro = TextField(default=None)

    def __unicode__(self):
        return '%s [%s]' % (self.qgroup_id, self.group_name)


class QGroupQuiz(Model):
    __slots__ = ['gq_id', 'qgroup', 'quiz', 'alias', 'priority', 'intro']
    gq_id = AutoField(primary_key=True)
    qgroup = ForeignKey(QGroup)
    quiz = ForeignKey(Quiz)
    alias = CharField(max_length=64, null=True)
    priority = PositiveSmallIntegerField(default=0, null=True)
    intro = TextField(default=None, null=True)

    def __unicode__(self):
        return '%s [%s]~[%s]' % (self.gq_id, self.qgroup.group_name, self.quiz.screen_name)


class Experiment(Model):
    __slots__ = ['experiment_id', 'name', 'qgroup', 'consent_file', 'priority', 'time_range', 'description']
    experiment_id = AutoField(primary_key=True)
    name = CharField(max_length=64)
    qgroup = ForeignKey(QGroup)
    consent_file = CharField(max_length=64)
    priority = PositiveSmallIntegerField(default=0)
    time_range = DateTimeRangeField()
    description = TextField(default=None)

    def __unicode__(self):
        return '%s [%s] - [%s]' % (self.experiment_id, self.name, self.qgroup.qgroup_id)


class UserFillQuiz(Model):
    __slots__ = ['fill_id', 'user', 'quiz', 'qgroup', 'fill_time', 'cost_seconds', 'ip_addr', 'location', 'answer', 'score', 'memo']
    fill_id = AutoField(primary_key=True)
    user = ForeignKey(User)
    quiz = ForeignKey(Quiz)
    qgroup = ForeignKey(QGroup)
    fill_time = DateTimeField(default=timezone.now)
    cost_seconds = IntegerField(default=-1)
    ip_addr = GenericIPAddressField(default=None, null=True)
    location = PointField(null=True)
    answer = HStoreField()
    score = HStoreField()
    memo = HStoreField(default=None, null=True)

    def __unicode__(self):
        return '[%s](%s:%s/%s)@%s{%ss}=>%s' % (self.fill_id, self.user.id, self.qgroup.group_name,
                                               self.quiz.screen_name, self.fill_time, self.cost_seconds, self.score)