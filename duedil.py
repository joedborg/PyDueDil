import json, urllib2

class Duedil(object):
    """
    Proveide the base class for the Duedil API.
    """
    def __init__(self, key):
        assert type(key) == str
        self._key = key
        self._url = "http://api.duedil.com/v2/"

    def __get__(self, params=""):
        assert type(params) == str
        return json.loads(urllib2.urlopen(self._url + params + "&api_key=" + self._key).read())['response']

    def __quote__(self, s):
        return urllib2.quote(s)
