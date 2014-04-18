#!/usr/bin/python
 # -*- coding: utf-8 -*-
from types import *
from config import api_func

def error_handler(fn):
    def wrapper(*args, **kwargs):
        try: 
            return fn(*args, **kwargs)
        except Exception as e:
            print(e)
    wrapper.__name__ = fn.__name__
    return wrapper

@error_handler
def check_arguments(fn_name, *args, **kwargs):
    params = {}
    if args:
        for x in args:
            if type(x) != DictType: 
                raise TypeError(
                    "Illegal argument {0}: Only named arguments or dictionary allowed" \
                        .format(x))
                return False
            params.update(x)
    (lambda: params.update(kwargs) if kwargs else {})()
    _illegal = [x for x in params.keys() if x not in api_func[fn_name]['params']]
    _missed  = [x for x in api_func[fn_name]['params'] \
                                            if x not in params.keys() \
                                            and x in api_func[fn_name]['required']]
    if _illegal or _missed:
        raise ArgumentError(fn_name, _illegal, _missed)
        return False
    return (lambda: params if params else {'format': 'json'})()

class ArgumentError(Exception):
    def __init__(self, name, illegal, missed):
        self.illegal = illegal 
        self.missed  = missed 
        self._name   = name
    def __str__(self):
        return repr(
            "ArgumentError: In function {0}: {1} {2})"\
                .format(self._name, 
                        (lambda: 'illegal arguments: {0},'\
                            .format(self.illegal) if self.illegal else '')(), 
                        (lambda: 'you miss required arguments: {0}'\
                            .format(self.missed) if self.missed else '')()))

class ConnectionError(Exception):
    def __init__(self, e):
        self.e = e
    def __str__(self):
        return repr(
            "Error: can't established connection with api.hipchat.com | {0}"\
                .format(self.e))

