import os, json, urllib2

class Duedil(object):
    """
    Proveide the base class for the Duedil API.
    """
    def __init__(self, key=None):
        self._key = self.__key__(key)
        self._url = "http://api.duedil.com/v2/"

    def __get__(self, params=""):
        assert type(params) == str
        return json.loads(urllib2.urlopen(self._url + params + "&api_key=" + self._key).read())['response']

    def __quote__(self, s):
        return urllib2.quote(s)

    def __key__(self, key):
        if key:
            with open("%s/.pyduedil_key" % (os.path.expanduser("~/")), "w") as f:
                f.write(key)
                return key
        try:
            with open("%s/.pyduedil_key" % (os.path.expanduser("~/"))) as f:
                return f.read()
        except IOError:
            raise RuntimeError("No key specified and no key file found")