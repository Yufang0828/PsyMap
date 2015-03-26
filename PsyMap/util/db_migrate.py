# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

import psycopg2
from quiz.dbutil import get_cur, get_cur_pg


curMY = get_cur()
curPG = get_cur_pg()


def migrate_quiz():
    curMY.execute('SELECT * FROM quiz')

    x = lambda i: r[i].encode('UTF-8')
    data = []
    for r in curMY:
        data.append( (x('QuizId'), x('ScreenName'), x('XmlPath'), x('Intro')) )
    sql = 'INSERT INTO "PsyMap_quiz" VALUES (%s,%s, %s, %s, NULL )'
    curPG.executemany(sql, data)

def migrate_qgroup():
    curMY.execute('SELECT * FROM qgroup')

    x = lambda i: r[i].encode('UTF-8') if isinstance(r[i],basestring) else r[i]
    data = []
    for r in curMY:
        data.append( (x('QGroupId'), x('GroupName'), x('Priority'), x('Intro')) )
    sql = 'INSERT INTO "PsyMap_qgroup" ("qgroup_id","group_name","priority","intro") VALUES (%s,%s, %s, %s )'
    curPG.executemany(sql, data)


def migrate_experiment():
    curMY.execute('SELECT * FROM experiment')

    x = lambda i: r[i].encode('UTF-8') if isinstance(r[i], basestring) else r[i]
    y = lambda r: '[%s,%s]' % (r['BeginTime'], r['EndTime'])
    data = []
    for r in curMY:
        data.append((x('ExperimentId'), x('Name'), x('AgreementFile'), x('Priority'), y(r), x('Description'), x('QGroupId')))
    sql = 'INSERT INTO "PsyMap_experiment" ("experiment_id","name","consent_file","priority","time_range","description","qgroup_id") VALUES (%s,%s, %s,%s,%s,%s,%s )'
    curPG.executemany(sql, data)


def migrate_qgroupquiz():
    curMY.execute('SELECT * FROM qgroupquiz')

    x = lambda i: r[i].encode('UTF-8') if isinstance(r[i], basestring) else r[i]
    data = []
    for r in curMY:
        data.append((x('GQId'), x('Alias'), x('InGroupOrder'), x('Intro'), x('QGroupId'), x('QuizId')))
    sql = 'INSERT INTO "PsyMap_qgroupquiz" ("gq_id","alias","priority","intro","qgroup_id","quiz_id") VALUES (%s,%s, %s,%s,%s,%s)'
    curPG.executemany(sql, data)


def migrate_users():
    curMY.execute('SELECT * FROM users')

    x = lambda i: r[i].encode('UTF-8') if isinstance(r[i], basestring) else r[i]
    first_name = lambda r: x('NickName') if x('NickName') is not None else 'Weibo User'
    data = []
    for r in curMY:
        data = (x('UserId'), x('LastActivityDate'), x('Login'), first_name(r), x('CreationDate'))
        sql = 'INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined") VALUES ' \
              '(%s,NULL,%s,False,%s,%s,NULL, NULL, False, True, %s)'
        try:
            curPG.execute(sql, data)
        except psycopg2.IntegrityError as e:
            print e

from shapely.geometry import Point

def migrate_userfillquiz():
    curMY.execute('SELECT * FROM userfillquiz where FillId<10')

    x = lambda i: r[i].encode('UTF-8') if isinstance(r[i], basestring) else r[i]

    def convert(i):
        w = ['"' + j.replace('"', '\\"').replace('@', '"=>"', 1) + '"' for j in i[1:].split('#')]
        return ','.join(w).encode('UTF-8')

    ans = lambda r: convert(r['Answer'])
    score = lambda r: convert(r['Score'])
    memo = lambda r: None if r['Memo'] is None else ('"User-Agent"=>"%s"' % r['Memo'])

    sql = 'INSERT INTO "PsyMap_userfillquiz" ("fill_id","fill_time","cost_seconds","ip_addr","location","answer","score", "memo", "qgroup_id", "quiz_id", "user_id") VALUES' \
          ' (%s,%s,%s,%s,ST_SetSRID(ST_MakePoint(%s, %s), 4326),%s,%s,%s,%s,%s,%s)'
    for r in curMY:
        print x('FillTime')
        data = ((x('FillId'), x('FillTime'), x('CostSeconds'), x('IPAddr'), x('Pos_Lng'), x('Pos_Lat'), ans(r), score(r), memo(r), x('QGroupId'), x('QuizId'), x('UserId')))
        curPG.execute(sql, data)


if __name__ == '__main__':
    # migrate_quiz()
    # migrate_qgroup()
    # migrate_experiment()
    # migrate_qgroupquiz()
    # migrate_users()
    migrate_userfillquiz()