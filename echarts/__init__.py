# coding: utf-8
__version__ = '0.1'
__author__ = 'Peter Howe <haobibo@gmail.com>'

__all__ = ['EChart', 'Axis', 'Polar', 'Legend', 'Tooltip', 'Series',
           'Line', 'Bar', 'Scatter', 'KLine', 'Pie', 'Radar', 'Chord', 'Force', 'Map', 'Gauge']

from .option import Base
from .option import Axis, Polar, Legend, Tooltip, Series
from .datastructure import *


class EChart(Base):
    def __init__(self, title, description=None, link=None, **kwargs):
        self.title = {
            'text': title,
            'subtext': description,
            'sublink': link
        }
        self.series = []

    def use(self, obj):
        if isinstance(obj, Axis):
            if obj.position in ('bottom', 'top'):
                if not hasattr(self, 'x_axis'):
                    setattr(self, 'x_axis', [])
                self.x_axis.append(obj)
            else:
                if not hasattr(self, 'y_axis'):
                    setattr(self, 'y_axis', [])
                self.y_axis.append(obj)
        elif isinstance(obj, Polar):
            if not hasattr(self, 'polar'):
                setattr(self, 'polar', [])
            self.polar.append(obj)
        elif isinstance(obj, Series):
            self.series.append(obj)
        else:  # anything else except Series and Axis
            setattr(self, obj.__class__.__name__.lower(), obj)

        return self

    @property
    def data(self):
        return self.series

    @property
    def json(self):
        """JSON format data."""
        j = {
            'title': self.title,
            'series': list(map(dict, self.series)),
        }

        if not hasattr(self, 'legend'):
            self.legend = Legend(list(map(lambda o: o.name, self.data)))

        j['legend'] = self.legend.json

        if hasattr(self, 'tooltip'):
            j['tooltip'] = self.tooltip.json
        if hasattr(self, 'x_axis'):
            j['xAxis'] = list(map(dict, self.x_axis))
        if hasattr(self, 'x_axis'):
            j['yAxis'] = list(map(dict, self.y_axis))
        if hasattr(self, 'polar'):
            j['polar'] = list(map(dict, self.polar))
        return j