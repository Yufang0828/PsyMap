__author__ = 'Peter_Howe<haobibo@gmail.com>'

import os
import json
import codecs
from collections import OrderedDict
from lxml import etree

import dbutil

base_dir = os.path.dirname(os.path.realpath(__file__))


def wrap_path(path):
    if path[0] == '.':
        path = os.path.join(base_dir, path)
    return path


def validate_xml(xml_file, dtd_file='./quiz/Questionnaire.dtd'):
    with open(wrap_path(xml_file), 'r') as f_xml:
        root = etree.XML(f_xml.read())

    validate = False
    dtd = None
    with open(wrap_path(dtd_file), 'r') as f_dtd:
        try:
            dtd = etree.DTD(f_dtd)
            validate = dtd.validate(root)
        except Exception as e:
            msg = e
            if dtd is not None:
                msg += ' \n ' + dtd.error_log.filter_from_errors()

        if not validate:
            raise ValueError(msg)
        return validate


def load_from_db():
    result = OrderedDict()
    cur = dbutil.get_cur()
    cur.execute('SELECT * FROM Quiz ORDER BY QuizId')
    for r in cur:
        qid = r.pop('QuizId')
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
    # return load_from_db()
    return load_from_json()


if __name__ == '__main__':
    dump_db_to_json()