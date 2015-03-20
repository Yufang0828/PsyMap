# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

import sys
import codecs
from collections import OrderedDict, namedtuple
from datetime import datetime

import dbutil
from quiz import QService

dimensions = OrderedDict()
users = dict()

quiz_with_answer = ['BJ_Demographic']

Fill = namedtuple('Fill',
    'fill_id, user_id, quiz_id, grp_id, fill_time, answer, cost_seconds, score, ip_addr, pos_lat, pos_lng, site_type, site_uid')


def parse(r):
    x = lambda i: r.get(i)
    f = Fill(x('FillId'), x('UserId'), x('QuizId'), x('QGroupId'), x('FillTime'), x('Answer'),
             x('CostSeconds'), x('Score'), x('IPAddr'), x('Pos_Lat'), x('Pos_Lng'), x('SiteType'), x('SiteUid'))
    return f


def get_user_fill_quiz(local_uid=None, site_type=None, site_uid=None, quiz_id=None):
    assert not ((local_uid is None) and (site_type is None or site_uid is None))
    local_uid = 'NULL' if local_uid is None else long(local_uid)
    site_type = 'NULL' if site_type is None else "'%s'" % site_type
    site_uid = 'NULL' if site_uid is None else long(site_uid)
    quiz_id = 'NULL' if quiz_id is None else "'%s'" % quiz_id

    cur = dbutil.get_cur()
    cur.execute('CALL P_GetUserFillQuiz(%s,%s,%s,%s)' % (local_uid, site_type, site_uid, quiz_id))
    for r in cur:
        f = parse(r)
        return f


def get_exp_fills(_exp_id):
    cur = dbutil.get_cur()
    cur.execute('CALL P_GetExpFills(%s,null,null)' % _exp_id)
    for r in cur:
        f = parse(r)

        quiz = QService.get_quiz(f.quiz_id)
        ss = quiz.score(f.answer, col_name=f.quiz_id)

        u = users.get(f.site_uid)
        if u is None:
            u = OrderedDict()
        u.update(ss)
        for s in ss:
            dimensions[s] = 0

        if f.quiz_id in quiz_with_answer:
            answers = quiz.parse(f.answer, col_name=f.quiz_id)
            u.update(answers)
            for a in answers:
                dimensions[a] = 0

        dim_cost_seconds = '%s_CostSeconds' % f.quiz_id
        dim_fill_time = '%s_FillTime' % f.quiz_id

        u[dim_cost_seconds] = f.cost_seconds
        u[dim_fill_time] = datetime.strftime(f.fill_time, '%Y/%m/%d %H:%M:%S')

        dimensions[dim_cost_seconds] = 0
        dimensions[dim_fill_time] = 0

        users[f.site_uid] = u


def export_expeiment():
    exp_id = 0

    print sys.argv

    if len(sys.argv) <= 1:
        print('Usage: python export.py exp_id [output_file_path]')
        exit()

    if len(sys.argv) > 1:
        exp_id = int(sys.argv[1])

    if len(sys.argv)>2:
        fpath = sys.argv[2]
        try:
            fp = codecs.open(fpath, 'w', 'utf-8')
            fp.write(u'\uFEFF')
            sys.stdout = fp
        except:
            raise RuntimeError('Unable to open file [%s] to write.' % fpath)

    get_exp_fills(exp_id)

    header = "SinaUid,"
    for dim in dimensions:
        header += "%s," % dim
    print header

    for u, scores in users.iteritems():
        line = '%s,' % u
        for dim in dimensions:
            line += '%s,' % scores.get(dim, '')

        print line


if __name__ == '__main__':
    def get_u_demo(sina_uid):
        s = get_user_fill_quiz(site_type='SINA', site_uid=sina_uid, quiz_id='Q2_Demographic')
        age, gender = s.answer.split('#q3')[0].split('#')[1:]
        return (age.split('@')[1].strip('[]'),gender.split('@')[1])

    path = "E:/WordCloud/users_list.txt"
    with codecs.open(path, 'r') as fp:
        for line in fp:
            uid = line.strip(' \t\r\n')
            age, gender = get_u_demo(uid)
            print uid, age.strip(' \t\r\n'), gender.strip(' \t\r\n')