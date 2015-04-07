# coding=utf-8
from urlparse import urlparse
from requests import PreparedRequest

from functools import wraps


def retry(max_tries, exceptions=(Exception,), hook=None):
    """Retry calling the decorated function
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            tries = max_tries
            while tries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions, e:
                    if hook is not None:
                        hook(e)
                    tries -= 1
            return f(*args, **kwargs)

        return f_retry  # true decorator
    return deco_retry


def parse_querystring(string):
    if '?' in string:
        string = urlparse(string).query
    return dict([item.split('=', 1) for item in string.split('&')])


def request_url(url, params):
    pre = PreparedRequest()
    pre.prepare_url(url, params)
    return pre.url