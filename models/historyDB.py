

from google.appengine.ext import ndb


class History(ndb.Model):

    symbol = ndb.StringProperty()
    enterprice = ndb.StringProperty()
    stoplose = ndb.StringProperty()
    takeprofit = ndb.StringProperty()
    profitorloss = ndb.StringProperty()
    volume = ndb.StringProperty()
    lstype = ndb.StringProperty()
    date = ndb.StringProperty()
    remarks = ndb.StringProperty()
    username = ndb.StringProperty()
    avatar = ndb.BlobProperty()

    @staticmethod
    def getHistory():
        return History.query()


