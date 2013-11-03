PyDueDil
========
A Python bind to the DueDil API

Installation
------------
To install, clone to the site-packages directory, or any other in the PYTHONPATH.

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

{'_id': '04533788',
 '_key': 'mfvzb5fbs452g2tvdd3gdgf2',
 '_url': 'http://api.duedil.com/v2/company/04533788.json?',
 'accountsType': u'0',
 'companyType': u'Private limited with share capital',
 'creditRatingLatestDescription': u'Company is dissolved',
 'directorsTotal': 4,
 'directorshipsClosed': 3,
 'directorshipsClosedDirector': 2,
 'directorshipsClosedSecretary': 1,
 'directorshipsRetired': 2,
 'directorshipsRetiredDirector': 1,
 'directorshipsRetiredSecretary': 1,
 'directorshipsTotal': 5,
 'id': u'04533788',
 'incorporationDate': u'2002-09-12',
 'latestAnnualReturnDate': u'2003-09-12',
 'name': u'GOOGLE LIMITED',
 'regAddress1': u'176 THE MOUNT',
 'regAddress2': u'GELDERD ROAD',
 'regAddress3': u'LEEDS',
 'regAddressPostcode': u'LS12 6DL',
 'regAreaCode': u'LS12',
 'regTps': u'N',
 'sicCode': u'7487',
 'sicCodesCount': 1,
 'sicDescription': u'Other business activities not elsewhere classified',
 'status': u'Dissolved',
 'tradingAddress1': u'176 The Mount',
 'tradingAddress2': u'Gelderd Road',
 'tradingAddress4': u'Leeds',
 'tradingAddressPostcode': u'LS12 6DL'}
```
