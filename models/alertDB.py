

from google.appengine.ext import ndb


class Alert(ndb.Model):
    symbol = ndb.StringProperty()
    enterprice = ndb.StringProperty()
    stoplose = ndb.StringProperty()
    takeprofit = ndb.StringProperty()
    volume = ndb.StringProperty()
