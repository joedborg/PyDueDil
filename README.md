PyDueDil
========
A Python bind to the DueDil API

Usage
-----
To search for companies, returning a list of dictionaries...
```python
>>> import pyduedil
>>> API_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaa'
>>> pyduedil.Companies(API_KEY).search('Google')

{u'data': [{u'id': u'04533788',
   u'locale': u'uk',
   u'name': u'Google Limited',
   u'uri': u'http://api.duedil.com/v2/company/04533788'},
  {u'id': u'05220885',
   u'locale': u'uk',
   u'name': u'Google Limited',
   u'uri': u'http://api.duedil.com/v2/company/05220885'},
  {u'id': u'06770815',
   u'locale': u'uk',
   u'name': u'Google Limited',
   u'uri': u'http://api.duedil.com/v2/company/06770815'},
  {u'id': u'08291317',
   u'locale': u'uk',
   u'name': u'Googled Limited',
   u'uri': u'http://api.duedil.com/v2/company/08291317'},
  {u'id': u'03977902',
   u'locale': u'uk',
   u'name': u'Google Uk Limited',
   u'uri': u'http://api.duedil.com/v2/company/03977902'}],
 u'pagination': u'http://api.duedil.com/v2/search/companies?total_results=66&limit=5&offset=5&query=Google'}
```

Then use the id to create a company instance...
```python
>>> google = pyduedil.Company(API_KEY, '04533788')
```
...this creates an object with attributes...
```python
google.accountsType                   google.directorshipsTotal             google.regTps
google.companyType                    google.id                             google.sicCode
google.creditRatingLatestDescription  google.incorporationDate              google.sicCodesCount
google.directorsTotal                 google.latestAnnualReturnDate         google.sicDescription
google.directorshipsClosed            google.name                           google.status
google.directorshipsClosedDirector    google.regAddress1                    google.tradingAddress1
google.directorshipsClosedSecretary   google.regAddress2                    google.tradingAddress2
google.directorshipsRetired           google.regAddress3                    google.tradingAddress4
google.directorshipsRetiredDirector   google.regAddressPostcode             google.tradingAddressPostcode
google.directorshipsRetiredSecretary  google.regAreaCode

>>> google.companyType

u'Private limited with share capital'
```
...or, to get a dictionary, use...
```python
>>> google = pyduedil.Company(API_KEY, '04533788').__dict__
```