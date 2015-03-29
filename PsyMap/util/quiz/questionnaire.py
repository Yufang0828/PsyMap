# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

import os
from collections import OrderedDict, namedtuple, defaultdict

from lxml import etree

import meta


__all__ = ['Answer', 'Tag', 'Remark', 'Question', 'Questionnaire', 'QService']

Answer = namedtuple('Answer', 'aid, score, content, type')
Tag = namedtuple('Tag', 'name, label, info')
Remark = namedtuple('Remark', 'tag, min_score, max_score, info')


class Question:
    __slots__ = ['qid', 'title', 'tag', 'type', 'restriction', 'answers']

    """Class for each question in a questionnaire"""
    def __init__(self, qid, title=None, tag=None, _type='_def', restriction=None):
        self.qid, self.title, self.tag, self.type, self.restriction = qid, title, tag, _type, restriction
        self.answers = OrderedDict()

    def add_answer(self, aid, score=0, content=None, _type=None):
        self.answers[aid] = Answer(aid, score, content, _type)

    def get_answer_score(self, aid):
        a = self.answers.get(aid, None)
        return a.score if a is not None else 0

    def get_answer_content(self, aid):
        a = self.answers.get(aid, None)
        return a.content if a is not None else aid

    def to_dict(self):
        return {
            'qid': self.qid,
            'title': self.title,
            'tag': self.tag,
            'type': self.type,
            'restriction': self.restriction,
            'answers': self.answers
        }


class Questionnaire:
    """Class for a questionnaire"""
    __slots__ = ['quiz_id', 'xml', 'identifier', 'caption', 'information', 'questions', 'tags', 'remarks']

    def __init__(self, quiz_id, xml_path):
        self.quiz_id, self.xml = quiz_id, xml_path
        self.questions = OrderedDict()
        self.tags = {}
        self.remarks = defaultdict(list)

        x = etree.parse(xml_path).getroot()

        # Setting description
        f = lambda i: setattr(self, i, x.xpath('//' + i)[0].text)
        map(f, ['identifier', 'caption', 'information'])

        # Setting questions
        for q_node in x.xpath('//questions/question'):
            title = q_node.xpath('./title')[0].text
            qid, tag, _type = q_node.get('qid'), q_node.get('tag', '_def'), q_node.get('type', 'single')

            restriction = q_node.xpath('./restriction')
            restriction = restriction[0].attrib if len(restriction) > 0 else None
            _q = Question(qid, title, tag, _type, restriction)

            for a in q_node.xpath('./answer'):
                aid, score, _type, text = a.get('aid'), a.get('score'), a.get('type', None), a.text
                _q.add_answer(aid, score, content=text, _type=_type)

            self.questions[qid] = _q

        # Setting categories (tags)
        for tag in x.xpath('//tags/tag'):
            name, label, info = tag.get('name', '_def'), tag.get('label', self.caption), tag.text
            self.tags[name] = Tag(name, label, info)

        # Setting remarks
        for r in x.xpath('//remarks/remark'):
            tag, min_score, max_score, info = r.get('tag', '_def'), r.get('minScore', 0), r.get('maxScore', 0), r.text
            self.remarks[tag].append(Remark(tag, min_score, max_score, info))

    def parse_legacy(self, str_answer, translate_question=False, translate_answer=False, prefix=None):
        result = OrderedDict()
        for l in str_answer.split('#'):
            qid, ans = l.split('@')
            ans = ans.strip(' \t\r\n[],')
            q = self.questions[qid]

            key = '%s%s' % (
                (prefix + '_') if prefix is not None else '',  # if has prefix
                q.title if translate_question else qid          # if translate qid to question title
            )
            result[key] = q.get_answer_text(ans, ans) if translate_answer else ans
        return result

    def score(self, dic_ans):
        # Given an answer dict, calculate the quiz score according to xml questionnaire file.
        result = defaultdict(float)
        for qid, aid in dic_ans.iteritems():
            q = self.questions[qid]
            result[q.tag] += float(q.get_answer_score(aid))
        return result

    def remark(self, dic_score):
        def convert_score(s, _tag=None):
            m = {'min': float('-inf'), 'max': float('inf'), 'avg': QService.get_norm(self.quiz_id)[_tag]}
            try:
                return m[str(s).lower()]
            except KeyError:
                return float(s)

        result = {}
        for tag, score in dic_score.iteritems():
            for r in self.remarks[tag]:
                _min, _max = convert_score(r.min_score, _tag=tag), convert_score(r.max_score, _tag=tag)
                if _min <= float(score) < _max:
                    result[tag] = r
        return result


class QService:
    quiz_cache = {}
    norm_cache = {}

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
            quiz = QService.quiz_cache[quiz_id]
        except KeyError:
            xml_path = self.get_xml_path(quiz_id)
            meta.validate_xml(xml_path)
            quiz = Questionnaire(quiz_id, xml_path)
            QService.quiz_cache[quiz_id] = quiz
        return quiz

    @staticmethod
    def get_norm(quiz_id):
        try:
            norm = QService.norm_cache[quiz_id]
        except KeyError:
            norm = meta.load_quiz_norm(quiz_id)
            if norm is None:
                tags = QService().get_quiz(quiz_id).tags.keys()
                if len(tags) == 0:
                    tags = ['_def']
                norm = dict(zip(tags, [0]*len(tags)))
            QService.norm_cache[quiz_id] = norm
        return {k: float(v) for k, v in norm.iteritems()}

    @staticmethod
    def get_char_data(quiz_id, scores):
        from echarts import *
        return BFI44(scores)


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