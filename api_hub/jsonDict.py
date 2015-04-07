# coding=utf-8
import json
import re

class JsonDict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'JsonDict' object has no attribute '%s'" % attr)

    def __setattr__(self, attr, value):
        self[attr] = value


def loads(string):
    return json.loads(string, object_hook=lambda pairs: JsonDict(pairs.iteritems()))


def get_values(dic, attr_pattern):
    regex = re.compile(attr_pattern)
    result = {}
    for k, v in dic.iteritems():
        if isinstance(v, dict):
            result.update(get_values(v, attr_pattern))
        elif re.match(regex, k):
            result[k] = v
    return result