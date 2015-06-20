# -*- coding: UTF-8 -*-
__author__ = 'Gao Yuanbo'

from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField

class UserEmotion(Model):
    __slots__ = ['status_id', 'user', 'timestamp', 'location','ip_addr','emotion', 'source']

    status_id = AutoField(primary_key=True)
    user = ForeignKey(User)
    timestamp = DateTimeField(null=True)
    ip_addr = GenericIPAddressField(default=None, null=True)
    location = PointField(null=True,geography=True)
    emotion = CharField(max_length=32)
    source = CharField(max_length=32)  # 签到途径，例如微信、网页等
