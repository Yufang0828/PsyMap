# -*- coding: UTF-8 -*-
__author__ = 'Gao Yuanbo'

import json
import ast
import time,datetime
from django.http import HttpResponse
from django.shortcuts import render
from PsyMap.models.emotion import *
from django.contrib.gis.geos import GEOSGeometry

# from django.contrib.gis.gdal import OGRGeometry  # TODO: delete this line if not needed

from ..util.web import get_ip_from_request

def index(request, lat, long):
    page = 'PsyMap/emotion/checkin.html'
    return render(request,page,{
        'lat':lat,
        'long':long
    })


def checkin(request, lat, long, emotion, user_id=-1):  # TODO: 为什么设置为-1，应该从session中获取当前用户
    dict = {}
    deadtime = datetime.datetime.now()
    ip = get_ip_from_request(request)
    ulist =  UserEmotion.objects.filter(user_id=user_id)
    #user first sign in
    if len(list(ulist)) is 0:
       pass
    else:
        for u in ulist:
            times = datetime.datetime.now().strftime("%Y-%m-%d")+" 00:00:00"
            d = datetime.datetime.strptime(times,"%Y-%m-%d %H:%M:%S")
            time2 = time.mktime(d.timetuple()) # starttime
            time1 = time.mktime(u.timestamp.timetuple()) # current time
            if(time1 < time2):
                continue
            else:
                dict['msg'] = False
                j = json.dumps(dict)
                return HttpResponse(j)
    #user not today sign in
    saveuser(ip,user_id,lat,long,emotion)
    starttime = deadtime-datetime.timedelta(days = 1)
    return HttpResponse(signsuccess(lat,long,starttime,deadtime,user_id))

#save user
def saveuser(ip,user_id,lat,long,emotion):
    print 'ip :', ip
    u = UserEmotion.objects.create(user_id=user_id)
    u.ip_addr = ip
    u.location = GEOSGeometry('POINT('+lat+' '+long+')',srid=4326)
    u.timestamp = timezone.now()
    u.emotion = emotion
    u.save()

# obtain emotion check-ins with in 10kilometers
def signsuccess(lat, long, begin_time, end_time, uid):
    # TODO: Hao Bibo: whe long_ should -100 ? Use comments to explain why.
    lat_, long_ = float(lat), float(long)-100

    # TODO: Hao Bibo: 这里建议加一个LIMIT，万一此处的签到数量巨大，只显示最最近的1000个（或者更多）即可
    sql = 'SELECT * FROM "PsyMap_emotion" AS e WHERE e.timestamp between %s and %s ' \
          'AND earth_box(ll_to_earth(%s,%s),10000000) @> ll_to_earth(%s,%s)' \
          'ORDER BY e.timestamp DESC LIMIT 1000'
    emos = UserEmotion.objects.raw(sql, [begin_time, end_time, lat,long, lat_, long_])

    # TODO: comment this line after debug
    print "There are %s point near point (%s, %s)." % (len(list(emos)), lat_, long_ )

    # TODO: Hao Bibo: info 应该是一个list，而不是一个dict
    # TODO: 在这个list里，每个对象包含三个字段：lat、long、emotion
    # TODO: 请修改下面的代码，以及对应的前台逻辑
    info = {'lat': list(),'long': list(),'emotion': list()}

    for l in emos:
        lo = l.location
        j = ast.literal_eval(lo.json)
        eventlat,eventlong = j['coordinates'][0:1]
        info['lat'].append(eventlat)
        info['long'].append(eventlong)
        info['emotion'].append(l.emotion)

    ret = {
        'msg': True,
        'location': info
    }
    j = json.dumps(ret)
    return j