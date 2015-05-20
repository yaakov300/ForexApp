__author__ = 'AVIRAM'

import sys
sys.path.insert(0, 'lib')	#we need these two lines in order to make libraries imported from lib folder work properly
import requests
from google.appengine.ext import ndb

class Symbol(ndb.Model):
    symbol = ndb.StringProperty()
    price = ndb.IntegerProperty()

    def getPrice(symbolInput):
        sy = Symbol.query(Symbol.symbol==symbolInput).get()	#try to fetch today's word from db
        return sy.price

