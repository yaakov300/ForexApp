from google.appengine.ext import ndb

class symbolGraphDB(ndb.Model):
    SP = ndb.StringProperty()
    NSD = ndb.StringProperty()
    DAX = ndb.StringProperty()
    GOLD = ndb.StringProperty()
    COIL = ndb.StringProperty()
    ERU = ndb.StringProperty()
    JPY = ndb.StringProperty()
    CAD = ndb.StringProperty()
    GPB = ndb.StringProperty()
    AUD = ndb.StringProperty()
    NZE = ndb.StringProperty()
    CHF = ndb.StringProperty()
    ILS = ndb.StringProperty()

    #symbolPrice = ndb.StringProperty(repeated=True)

    @staticmethod
    def getsSymbolGraph():
        return symbolGraphDB.query()


