__author__ = 'Yaacov'

from google.appengine.api import users
from google.appengine.ext import ndb


class User(ndb.Model):
    userName = ndb.StringProperty()
    mail = ndb.StringProperty()
    password = ndb.StringProperty()
