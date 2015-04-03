# -*- coding: UTF-8 -*-
__author__ = 'Peter_Howe<haobibo@gmail.com>'

from collections import namedtuple

Chart = namedtuple('Chart', 'modules, data')


def draw(quiz_id, scores):
    return BFI44(scores)


def BFI44(scores):
    chart_data = {
        'title': {
            'text': '我的大五人格',
            'subtext': '由“心理地图”分析提供。',
            'x': 'center',
            'y': 'top'
        },
        'xAxis': [
            {
                'type': 'category',
                'data': ["外向性", "尽责性", "宜人性", "神经质", "开放性"]
            }
        ],
        'yAxis': [
            {
                'type': 'value'
            }
        ],
        'series': [
            {
                "name": "人格",
                "type": "bar",
                "data": [5, 20, 40, 10, 10]
            }
        ]
    }

    return Chart(['bar'], chart_data)