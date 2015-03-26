# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'


import datetime, dateutil.tz

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.gis.geos import GEOSGeometry

from PsyMap.util import web
from PsyMap.util.quiz.questionnaire import QService
from PsyMap.models.quiz import *


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


@require_http_methods(["POST"])
def submit(request):
    uid = request.session.get('u', 0)  #TODO None
    x = lambda i: request.POST.get(i)

    f = UserFillQuiz()
    for k in ['quiz_id', 'qgroup_id', 'cost_seconds', 'answer']:
        setattr(f, k, x(k))

    f.user_id = uid
    f.ip_addr = web.get_ip_from_request(request)
    f.memo = '"User-Agent"=>"%s"' % request.META.get('HTTP_USER_AGENT', 'Unknown')
    remote_host = request.META.get('HTTP_USER_HOST')
    if remote_host is not None:
        f.memo += ',"Remote-Host"=>"%s"' % remote_host
    f.location = GEOSGeometry('POINT(%s %s)' % (x('long'), x('lat')))  # POINT(longitude latitude)
    f.score = ""

    tz_client = dateutil.tz.tzoffset(None, int(x('tz')))
    f.fill_time = datetime.datetime.utcnow().replace(tzinfo=dateutil.tz.tzutc()).astimezone(tz_client)

    f.save()

    r = {
        'status': 'success',   # success, fail, no-login
        'fill_id': f.fill_id,  # fill_id after fill is inserted into UserFillQuiz
    }
    return JsonResponse(r)


#@require_http_methods(["POST"])
def result(request):
    fid = request.POST.get('fill_id', 16)  # TODO None
    f = UserFillQuiz.objects.get(fill_id=fid)
    r = {
        'quiz': qService.get_quiz(f.quiz_id),
        'answer': f.answer,
        'score': f.score
    }
    return render(request, 'PsyMap/quiz/result.html', r)