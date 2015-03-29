# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'


import json
import re
import datetime
import dateutil.tz

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.template.defaulttags import register
from django.template.defaultfilters import stringfilter

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


def fill(request, grp_id=0, quiz_id=None):
    quiz = qService.get_quiz(quiz_id)
    return render(request, 'PsyMap/quiz/fill.html', {
        'quiz_id': quiz_id,
        'grp_id': grp_id,
        'quiz': quiz
    })


@require_http_methods(["POST"])
def submit(request):
    uid = request.user.id
    if uid is None:
        return JsonResponse({'status': 'no-login'})

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
    ans = json.loads('{%s}' % f.answer.replace('=>', ':'), encoding='utf-8')
    score = QService().get_quiz(f.quiz_id).score(ans)   # type dict
    f.score = json.dumps(score).strip('{}').replace(':', '=>')  # hstore string

    tz_client = dateutil.tz.tzoffset(None, int(x('tz')))
    f.fill_time = datetime.datetime.utcnow().replace(tzinfo=dateutil.tz.tzutc()).astimezone(tz_client)

    f.save()

    r = {
        'status': 'success',   # success, fail, no-login
        'fill_id': f.fill_id,  # fill_id after fill is inserted into UserFillQuiz
    }
    return JsonResponse(r)


@register.filter
def get_tag_label(tags, name):
    t = tags.get(name)
    return t.label if t is not None else 'Thanks!'


@register.filter
def get_tag_info(tags, name):
    t = tags.get(name)
    return t.info if t is not None else ''


@register.filter
@stringfilter
def paragraphs(value):
    paras = re.split(r'[\r\n]+', value)
    paras = ['<p>%s</p>' % p.strip() for p in paras]
    return '\n'.join(paras)


#@require_http_methods(["POST"])
def result(request):
    uid = request.user.id
    fid = request.POST.get('fill_id', 32)

    if uid is None or fid is None:  # not login user or no fill_id submitted
        return render(request, 'PsyMap/quiz/index.html')

    f = None
    try:
        f = UserFillQuiz.objects.raw('SELECT fill_id, score::json FROM "PsyMap_userfillquiz" WHERE fill_id=%s', (fid,))[0]
    except Exception:
        pass

    if f is None or f.user_id != uid:   # fill not for this user
        return render(request, 'PsyMap/quiz/index.html')

    quiz = qService.get_quiz(f.quiz_id)
    remarks = quiz.remark(f.score)
    chart = QService.get_char_data(f.quiz_id, f.score)

    jsonify = lambda data: json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)

    r = {
        'quiz': quiz,
        'fill': f,
        'remarks': remarks,
        'chart': jsonify(chart.modules),
        'chart_data': jsonify(chart.data)
    }
    return render(request, 'PsyMap/quiz/result.html', r)