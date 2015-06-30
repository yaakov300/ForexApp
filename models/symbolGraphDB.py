from google.appengine.ext import ndb
from decimal import Decimal

class symbolGraphDB(ndb.Model):
    SP = ndb.StringProperty()
    NSD = ndb.StringProperty()
    DAX = ndb.StringProperty()
    GOLD = ndb.StringProperty()
    COIL = ndb.StringProperty()

    EUR = ndb.StringProperty()
    JPY = ndb.StringProperty()
    CAD = ndb.StringProperty()
    GPB = ndb.StringProperty()
    AUD = ndb.StringProperty()
    NZD = ndb.StringProperty()
    CHF = ndb.StringProperty()
    ILS = ndb.StringProperty()
    date = ndb.StringProperty()

    @staticmethod
    def getsSymbolGraph():
        return symbolGraphDB.query()

    @staticmethod
    def getByCul(symbol):
        array=[]
        temp=symbolGraphDB.query()
        for t in temp:
            if(symbol=="minSP"):
                value=t.SP
            if(symbol=="NSDQ"):
                value=t.NSD
            if(symbol=="DAX"):
                value=t.DAX
            if(symbol=="GOLD"):
                value=t.GOLD
            if(symbol=="C.OIL"):
                value=t.COIL

            if(symbol=="EUR"):
                value=t.EUR
            if(symbol=="JPY"):
                value=t.JPY

            array.append(value)
        return array

    @staticmethod
    def getCurrCROS(sFrom,sTo):
        arrCros=[]

        arrTo=symbolGraphDB.getByCul(sTo)
        arrFrom=symbolGraphDB.getByCul(sFrom)

        for x in range(len(arrTo)):
            cFrom=(Decimal(arrFrom[x]))
            cTo=(Decimal(arrTo[x]))

            value=cFrom/cTo
            value="{0:.4f}".format(value)
            arrCros.append(value)

        return  arrCros





