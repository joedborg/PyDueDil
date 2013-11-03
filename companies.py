from duodil import Duodil

_company_status_lookup = {
    "L": u"Live",
    "D": u"Dissolved",
    "R": u"Removed",
    "!": u"Deleted",
    "X": u"Converted / Closed"
}

_company_type_lookup = {
    "0": u"Other",
    "1": u"Private unlimited with share capital",
    "2": u"Private limited with share capital",
    "3": u"Public limited with share capital",
    "4": u"Old public limited company",
    "5": u"Private limited by guarantee without share capital, exempt from using 'Limited'",
    "6": u"Limited Partnership",
    "7": u"Private limited by guarantee without share capital",
    "8": u"Company converted / closed",
    "9": u"Unlimited / No share capital",
    "A": u"Limited"
}

_liquidation_status_lookup = {
    "L": u"In liquidation",
    "R": u"In receivership",
    "S": u"Strike off listed",
    "O": u"Struck off"
}

class Companies(Duodil):
    """
    Extend Duodil for companies.
    """
    def __init__(self, key):
         Duodil.__init__(self, key)
         self._url += "search/companies.json?"

    def search(self, query):
        query = self.__quote__(query)
        return self.__get__("query=%s" % (query))["data"]

class Company(Duodil):
    """
    Extend Duodil for a company.
    """
    def __init__(self, key, id):
        Duodil.__init__(self, key)
        self._id = id
        self._url += "company/%s.json?" % (self._id)
        get = self.__get__("fields=get_all")
        for key in get.iterkeys():
            if key == "status":
                self.__setattr__(key, _company_status_lookup[get[key]])
            elif key == "companyType":
                self.__setattr__(key, _company_type_lookup[get[key]])
            else:
                self.__setattr__(key, get[key])