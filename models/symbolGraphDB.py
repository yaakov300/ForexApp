from google.appengine.ext import ndb

class symbolGraph(ndb.Model):
    symbolPrice = ndb.StringProperty(repeated=True)

    @staticmethod
    def getsSymbolGraph():
        return symbolGraph.query()


