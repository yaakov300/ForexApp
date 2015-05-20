__author__ = 'Yaacov'


from google.appengine.ext import ndb


class User(ndb.Model):
    userName = ndb.StringProperty()
    mail = ndb.StringProperty()
    password = ndb.StringProperty()
