from duodil import Duodil

class Directors(Duodil):
    """
    Extend Duodil for directors.
    """
    def __init__(self, key):
        Duodil.__init__(self, key)
        self._url += "search/directors.json?"

    def search(self, query):
        query = self.__quote__(query)
        return self.__get__("query=%s" % (query))["data"]

class Director(Duodil):
    """
    Extend Duidil for a director.
    """
    def __init__(self, key, id):
        Duodil.__init__(self, key)
        self._url += "director/%s.json?" % (id)
        get = self.__get__("field=get_all")
        for key in get.iterkeys():
            self.__setattr__(key, get[key])