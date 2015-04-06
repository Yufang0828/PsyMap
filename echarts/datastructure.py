from .option import Series


class Line(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Line, self).__init__('line', name=name, data=data, **kwargs)


class KLine(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(KLine, self).__init__('k', name=name, data=data, **kwargs)


class Bar(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Bar, self).__init__('bar', name=name, data=data, **kwargs)


class Pie(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Pie, self).__init__('pie', name=name, data=data, **kwargs)


class Gauge(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Gauge, self).__init__('gauge', name=name, data=data, **kwargs)


class Scatter(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Scatter, self).__init__(
            'scatter', name=name, data=data, **kwargs
        )


class Radar(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Radar, self).__init__('radar', name=name, data=data, **kwargs)


class Force(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Force, self).__init__('force', name=name, data=data, **kwargs)


class Chord(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Chord, self).__init__('chord', name=name, data=data, **kwargs)


class Map(Series):
    def __init__(self, name=None, data=None, **kwargs):
        super(Map, self).__init__('map', name=name, data=data, **kwargs)
