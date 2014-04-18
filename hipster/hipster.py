#!/usr/bin/python
 # -*- coding: utf-8 -*-

import json, urllib3
from config import api_func
from errors import *
try:
    from urllib import  urlencode
except:
    from urllib.parse import urlencode

API_URL = 'https://api.hipchat.com/v1'

@error_handler
def singleton_with_methods(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            instances[class_].__init__(args[0])
            for key in api_func:
                _temp = (lambda **kwrgs: kwrgs)
                _temp.__name__ = key
                class_.__dict__[_temp.__name__] = call_api(
                    api_func[key]['method'], 
                    api_func[key]['API_url'])(_temp)
        return instances[class_]
    return getinstance

def call_api(method, dest):
    def decorator(fn):
        @error_handler
        def wrapper(self, *args, **kwargs):
            params = check_arguments(fn.__name__, *args, **kwargs)
            if params:
                url = '{0}/{1}?auth_token={2}&{3}'\
                    .format(API_URL, dest, self.AUTH_TOKEN, urlencode(params))
                try:
                    req = urllib3.PoolManager().urlopen(method, url)
                    return {
                        'status' : req.status,
                        'data'   : json.loads(req.data)\
                            if req.status == 200\
                            else req.data
                        }
                except Exception as e:
                    raise ConnectionError(e)
            wrapper.__name__ = fn.__name__
        return wrapper
    return decorator

