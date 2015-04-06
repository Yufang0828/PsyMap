import json


class Base(object):
    def __str__(self):
        """JSON stringify format data."""
        return json.dumps(self.json, sort_keys=True, indent=2)

    def __getitem__(self, key):
        return self.json.get(key)

    def keys(self):
        return self.json.keys()

    @property
    def json(self):
        raise NotImplementedError


class Axis(Base):
    """Axis data structure. http://echarts.baidu.com/doc/doc.html#Axis"""

    def __init__(self, _type, position, name='', data=None, **kwargs):
        assert _type in ('category', 'value', 'time')
        assert position in ('bottom', 'top', 'left', 'right')
        self.type, self.position, self.name, self.data, self._kwargs = _type, position, name, data or [], kwargs

    def __repr__(self):
        return 'Axis<%s/%s>' % (self.type, self.position)

    @property
    def json(self):
        """JSON format data."""
        j = dict(
            type=self.type,
            position=self.position,
            data=self.data
        )
        if self.name:
            j['name'] = self.name
        if self._kwargs:
            j.update(self._kwargs)
        return j


class Polar(Base):
    """Polar Data Structure http://echarts.baidu.com/doc/doc.html#Polar"""

    def __init__(self, _type, data=None, **kwargs):
        assert _type in ('polygon', 'circle')
        self.type, self.data, self._kwargs = _type, data or [], kwargs

    def __repr__(self):
        return 'Polar<%s/%s>' % (self.type, self.position)

    @property
    def json(self):
        """JSON format data."""
        j = dict(
            type=self.type,
            indicator=self.data
        )
        if self._kwargs:
            j.update(self._kwargs)
        return j


class Legend(Base):
    """Legend section for EChart."""
    def __init__(self, data, orient='vertical', position=None, **kwargs):
        assert orient in ('horizontal', 'vertical')
        if not position:
            position = ('right', 'bottom')
        self.data, self.orient, self.position, self._kwargs = data, orient, position, kwargs

    @property
    def json(self):
        """JSON format data."""
        j = {
            'data': self.data,
            'orient': self.orient,
            'x': self.position[0],
            'y': self.position[1]
        }

        if self._kwargs:
            j.update(self._kwargs)
        return j


class Tooltip(Base):
    """A tooltip when hovering."""
    def __init__(self, trigger='axis', **kwargs):
        assert trigger in ('axis', 'item')
        self.trigger, self._kwargs = trigger, kwargs

    @property
    def json(self):
        j = {
            'trigger': self.trigger,
        }
        if self._kwargs:
            j.update(self._kwargs)
        return j


class Series(Base):
    types = {'line', 'bar', 'scatter', 'k', 'pie', 'radar', 'chord', 'force', 'map', 'gauge'}

    def __init__(self, _type, name=None, data=None, **kwargs):
        assert _type in Series.types
        self.type, self.name, self.data, self._kwargs = _type, name, data or [], kwargs

    @property
    def json(self):
        j = {
            'type': self.type,
            'data': self.data
        }
        if self.name:
            j['name'] = self.name
        if self._kwargs:
            j.update(self._kwargs)
        return j
