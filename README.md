PyDueDil
========
A Python bind to the DueDil API

Installation
------------
To install, clone to the site-packages directory, or any other in the PYTHONPATH.

Usage
-----
When an API_KEY is specified, it is saved to `~/.pyduedil_key`, so isn't required after.  It will be overwritten if specified again.

To search for companies, returning a generator of Company instances...
```python
>>> from PyDueDil.companies import Companies
>>> API_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaa'
>>> Companies(API_KEY).search('Google')

<generator object search at 0x10a8d6870>
```

Then use the id to create a company instance...
```python
>>> google = Company('04533788', key=API_KEY)
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
>>> google = Company(API_KEY, '04533788').__dict__

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
