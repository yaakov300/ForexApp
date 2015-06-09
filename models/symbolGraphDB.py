from google.appengine.ext import ndb

class symbolGraph(ndb.Model):

    minSP = ndb.StringProperty()
    NSDQ = ndb.StringProperty()
    DAX = ndb.StringProperty()
    GOLD = ndb.StringProperty()
    C.OIL = ndb.StringProperty()
    EUR/USD = ndb.StringProperty()
    USD/JPY = ndb.StringProperty()
    USD/CAD = ndb.StringProperty()
    GBP/USD = ndb.StringProperty()
    AUD/USD = ndb.StringProperty()
    NZD/USD = ndb.StringProperty()
    USD/CHF = ndb.StringProperty()
    USD/ILS = ndb.StringProperty()
    EUR/AUD = ndb.StringProperty()
    EUR/NZD = ndb.StringProperty()
    EUR/CHF = ndb.StringProperty()
    EUR/JPY = ndb.StringProperty()
    EUR/CAD = ndb.StringProperty()
    EUR/GBP = ndb.StringProperty()
    GBP/AUD = ndb.StringProperty()
    GBP/JPY = ndb.StringProperty()
    GBP/NZD = ndb.StringProperty()
    GBP/CHF = ndb.StringProperty()
    AUD/NZD = ndb.StringProperty()
    AUD/CAD = ndb.StringProperty()
    NZD/JPY = ndb.StringProperty()
    NZD/CAD = ndb.StringProperty()
    CAD/JPY = ndb.StringProperty()
    CHF/JPY = ndb.StringProperty()

    @staticmethod
    def getsSymbolGraph():
        return symbolGraph.query()

