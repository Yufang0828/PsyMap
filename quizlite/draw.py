# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from collections import namedtuple

from echarts import *


Chart = namedtuple('Chart', 'modules, data')

desc = '由“心理地图”分析提供'
link = 'http://ccpl.psych.ac.cn/PsyMap/'


def chart_radar(caption, score, norm):
    polar = Polar('polygon', [{
        'text': norm[i].get('label'),
        'min': norm[i].get('min') * 0.9,
        'max': norm[i].get('max') * 1.1
    } for i in score.keys()])
    data = Radar(name=caption, data=[
        {'value': score.values(), 'name': '我的得分'},
        {'value': ['%.2f' % i.get('avg') for i in norm.values()], 'name': '大家的平均分'},
    ])
    legend = Legend([i.get('name') for i in data.data])

    c = EChart(caption, desc, link)
    c.use(data).use(polar).use(legend)
    return Chart(['radar'], c)


def chart_bar(caption, score, norm):
    x_axis = Axis('category', data=[norm[i].get('label') for i in score.keys()], position='bottom')
    y_axis = Axis('value', position='left')
    data_i = Bar(name='我的得分', data=score.values())
    data_norm = Bar(name='大家的平均分', data=['%.2f' % i.get('avg') for i in norm.values()])
    legend = Legend(['我的得分', '大家的平均分'])

    c = EChart(caption, desc, link)
    c.use(x_axis).use(y_axis).use(data_i).use(data_norm).use(legend)
    return Chart(['bar'], c)

drawer = {
    'BFI48': chart_radar,
    'BFI44': chart_radar,
}


def draw(quiz_id, caption, score, norm=None):
    f = drawer.get(quiz_id, chart_bar)
    title = u'我的%s结果' % caption
    return f(title, score, norm)