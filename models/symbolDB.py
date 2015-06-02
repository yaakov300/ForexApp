from google.appengine.ext import ndb


class Symbol(ndb.Model):
    symbol = ndb.StringProperty()
    price = ndb.StringProperty()

    @staticmethod
    def getSymbol():
        return Symbol.query()