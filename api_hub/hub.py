# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from collections import namedtuple

from api_hub.jsonDict import get_values


AppConfig = namedtuple('AppConfig', 'key, secret, redirect_uri')

cfgs = {
    'weibo':  AppConfig('2083434837', '0f0b491b53f93d73e19fbfc09b823728', 'http://ccpl.psych.ac.cn/PsyMap/accounts/callback/weibo'),
    'renren': AppConfig('842991772a904fcba75ff418c9734b49', '10b8d90ea5d84fcba7afaccbd04c6823', 'http://ccpl.psych.ac.cn/PsyMap/accounts/callback/renren'),
    'douban': AppConfig('0e9563ce7b25e16b2bc02b6b7171a441', '395fc362c0ba54cf', 'http://ccpl.psych.ac.cn/PsyMap/accounts/callback/douban'),
    'wechat': AppConfig('wx419b2a8c74a010c0', '6ec543cfadfdc716adaac90f87a49b31', '')
}


def import_from(module, name):
    module = __import__(module, fromlist=[name])
    return getattr(module, name)


def link(site, code):
    App = import_from('api_hub.%s.open' % site, 'App')
    OAuth2 = import_from('api_hub.%s.open' % site, 'OAuth2')
    app = App(**cfgs[site].__dict__)
    oauth2 = OAuth2(app)
    token = oauth2.access_token(code=code).__dict__
    tk = get_values(token, '^access_token$').values()
    uid = get_values(token, '\w*id').values()
    err = get_values(token, '\.*err\.*')
    return tk, uid, err