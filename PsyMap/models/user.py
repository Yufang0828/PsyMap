# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from collections import namedtuple

from django.db.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import transaction

__all_ = ['UserLink']

Alien = namedtuple('Alien', 'code, name, alias')
aliens = {
    'weibo': Alien('SINA', '微博', 'weibo'),
    'renren': Alien('RENN', '人人', 'renren'),
    'douban': Alien('DOUB', '豆瓣', 'douban'),
    'baidu': Alien('BIDU', '百度', 'baidu'),
    'wechat': Alien('WECHAT', '微信', 'wechat'),
    'qq': Alien('QQ', 'QQ', 'qq')
}


class UserLink(Model):
    __slots__ = ['link_id', 'user', 'site', 'alien', 'token', 'updated']
    link_id = AutoField(primary_key=True)
    user = ForeignKey(User)
    site = CharField(max_length=8)
    alien = CharField(max_length=64)
    token = CharField(max_length=256, null=True)
    updated = DateTimeField(null=True)

    def __unicode__(self):
        return '[%s]%s@%s~%s' % (self.link_id, self.alien, self.site, self.updated)

    @staticmethod
    def check_site(site):
        return aliens.get(site.lower())

    @staticmethod
    @transaction.atomic
    def link(site, alien, token):
        k = UserLink.objects.filter(site=site, alien=alien)
        now = timezone.now()
        u = None
        try:
            k = k[0]
            k.token, k.updated = token, now
            k.save(force_update=True)
            u = k.user
        except IndexError:  # this alien user has not been connected to the site
            name = '%s#%s' % (site.upper(), alien)[:30]
            u = User.objects.create(is_superuser=False, is_staff=False, is_active=False, username=name, first_name=name)
            k = UserLink.objects.create(user=u, site=site, alien=alien, token=token, updated=now)
        return u
