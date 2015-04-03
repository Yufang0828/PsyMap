__author__ = 'Peter_Howe<haobibo@gmail.com>'

import os
import json
import codecs
from collections import OrderedDict

from lxml import etree

import dbutil

def load_from_db():
    result = OrderedDict()
    cur = dbutil.get_cur()
    cur.execute('SELECT * FROM Quiz ORDER BY QuizId')
    for r in cur:
        qid = r.pop('QuizId')
        result[qid] = r
    return result


def load_from_db_pg():
    result = OrderedDict()
    cur = dbutil.get_cur_pg()
    cur.execute('SELECT * FROM "PsyMap_quiz" ORDER BY quiz_id')
    for r in cur.fetchall():
        qid = r.pop('quiz_id')
        result[qid] = r
    return result


def load_from_json():
    with codecs.open(wrap_path('./quiz/meta.data'), 'r', encoding='utf-8') as fp:
        result = json.load(fp, encoding='utf-8')
        return result


def dump_db_to_json():
    result = load_from_db()
    with codecs.open(wrap_path('./quiz/meta.data'), 'w', encoding='utf-8') as fp:
        json.dump(result, fp, ensure_ascii=False, sort_keys=True, encoding='utf-8', indent=1)


def load_quiz_info():
    # return load_from_db_pg()
    # return load_from_db()
    return load_from_json()


if __name__ == '__main__':
    dump_db_to_json()