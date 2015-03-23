# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from django.shortcuts import render

from PsyMap.util.quiz.questionnaire import QService

qService = QService()


def index(request, page='index'):
    print page
    if page not in {'index', 'fill', 'results'}:
        page = 'index'
    return render(request, 'PsyMap/quiz/%s.html' % page)


def fill(request, grp_id=None, quiz_id=None):
    quiz = qService.get_quiz(quiz_id)
    return render(request, 'PsyMap/quiz/fill.html', {
        'quiz_id': quiz_id,
        'grp_id': grp_id,
        'quiz': quiz
    })