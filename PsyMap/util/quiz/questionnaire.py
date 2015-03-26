# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

import os
from collections import OrderedDict, namedtuple

from lxml import etree

import meta


Answer = namedtuple('Answer', 'aid, score, content, type')


class Question:
    __slots__ = ['qid', 'title', 'tag', 'type', 'restriction', 'answers']

    """Class for each question in a questionnaire"""
    def __init__(self, qid, title=None, tag=None, _type=None, restriction=None):
        self.qid, self.title, self.tag, self.type, self.restriction = qid, title, tag, _type, restriction
        self.answers = OrderedDict()

    def to_dict(self):
        return {
            'qid': self.qid,
            'title': self.title,
            'tag': self.tag,
            'type': self.type,
            'restriction': self.restriction,
            'answers': self.answers
        }

    def add_answer(self, aid, score, content=None, _type=None):
        self.answers[aid] = Answer(aid, score, content, _type)

    def get_answer_score(self, aid):
        return self.answers[aid].score

    def get_answer_content(self, aid):
        return self.answers[aid].content


class Questionnaire:
    """Class for a questionnaire"""
    def __init__(self, quiz_id, xml_path):
        self.quiz_id, self.xml = quiz_id, xml_path

        x = etree.parse(xml_path).getroot()
        f = lambda i: setattr(self, i, x.xpath('//' + i)[0].text)

        map(f, ['identifier', 'caption', 'information'])

        # Setting questions
        self.questions = OrderedDict()
        questions = x.xpath('//questions/question')
        for q_node in questions:
            title = q_node.xpath('./title')[0].text
            qid = q_node.get('qid')
            tag = q_node.get('tag')
            _type = q_node.get('type', 'single')
            restriction = q_node.xpath('./restriction')
            if len(restriction) > 0:
                restriction = restriction[0].attrib
            else:
                restriction = None
            _q = Question(qid, title, tag, _type, restriction)

            for a in q_node.xpath('./answer'):
                aid = a.get('aid')
                score = a.get('score')
                _type = a.get('type', None)
                text = a.text
                _q.add_answer(aid, score, content=text, _type=_type)

            self.questions[qid] = _q

    def parse(self, str_answer, translate_question=True, translate_answer=True, col_name=None):
        result = OrderedDict()

        ll = str_answer.split('#')
        for l in ll:
            if len(l) == 0:
                continue
            a = l.split('@')
            key_ = key = a[0]
            value_ = value = a[1].strip(' \t\r\n[]')

            tmp_q = self.questions.get(key, None)

            if col_name is not None:
                if key == '_def':
                    key_ = col_name
                else:
                    if translate_question:
                        key_ = tmp_q.title if tmp_q is not None else key

                    key_ = "%s_%s" % (col_name, key_)

            if translate_answer and tmp_q is not None:
                value_ = tmp_q.get_answer_text(value)

            result[key_] = value_
        return result

    def score(self, str_answer, col_name=None):
        # Given an answer str s, parse the string and calculate the quiz according to xml questionnaire file.
        dimensions = dict()

        ans = self.parse(str_answer, translate_answer=False, translate_question=False)
        for qid, aid in ans.iteritems():

            _q = self.questions.get(qid)
            if _q is None:
                continue

            tag = _q.tag
            score = _q.get_answer_score(aid)

            s_old = dimensions.get(tag, 0)
            dimensions[tag] = s_old + int(score)

        if col_name is not None:
            r_dimensions = OrderedDict()
            for tag, score in dimensions.iteritems():
                key = col_name if tag is None or tag == '_def' else"%s_%s" % (col_name, tag)
                r_dimensions[key] = score

            dimensions = r_dimensions

        return dimensions


class QService:
    cache = {}

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.quiz_meta = meta.load_quiz_info()

    def get_xml_path(self, quiz_id):
        try:
            q_info = self.quiz_meta[quiz_id]
            xml_path = q_info['XmlPath']
        except KeyError:
            raise RuntimeError('Cannot find XML path for quiz [%s]!' % quiz_id)

        return meta.wrap_path(xml_path)

    def get_quiz(self, quiz_id):
        try:
            quiz = QService.cache[quiz_id]
        except KeyError:
            xml_path = self.get_xml_path(quiz_id)
            meta.validate_xml(xml_path)
            quiz = Questionnaire(quiz_id, xml_path)
            QService.cache[quiz_id] = quiz

        return quiz


def unit_test(quiz_id):
    """
    >>> unit_test('Soc_GOV')

    >>> unit_test('Q1_Cyber')
    """
    for qid, q in QService().get_quiz(quiz_id).questions.iteritems():
        print q.to_dict()

if __name__ == '__main__':
    import doctest
    doctest.testmod()