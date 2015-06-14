import threading
from models.symbolGraphDB import symbolGraphDB
from threading import Lock

from lib import requests   #Used for http requests
import webapp2
import logging
from datetime import datetime
import time

stComm="ESM15.CME,NQM15.CME,^GDAXI,GCM15.CMX,CLN15.NYM"
stCurr="EURUSD,JPYUSD,CADUSD,GBPUSD,AUDUSD,NZDUSD,CHFUSD,ILSUSD"
mutex = Lock()
class symbolGraph(webapp2.RequestHandler):

    def get(self):
        logging.info('from the get')
        self.threading_minuets()

    def threading_minuets(self):
        threadArr = []
        '''
        for i in range(6):
            t = threading.Thread(target=self.multiRequests, args=(i,))
            threadArr.append(t)
        '''
        for i in range(6):
            t = threading.Timer(10*i, self.multiRequests)
            threadArr.append(t)

        for t in threadArr:
            t.start()
        for t in threadArr:
            t.join()

        logging.info('end threading_minuets')

    #this function get all price for commodities and currency from yahoo api.
    def multiRequests(self):
        logging.info('from the multiRequests')

        URLComm="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+stComm+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
        URLCurr="http//query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22"+stCurr+\
            "%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
        requestComm = requests.get(URLComm)
        dataComm = requestComm.json()#["query"]["results"]["quote"]["Ask"]
        requestCurr = requests.get(URLCurr)
        dataCurr = requestCurr.json()#["query"]["results"]["rate"]["Rate"]

        sp = dataComm["query"]["results"]["quote"][0]["Ask"]
        nsd = dataComm["query"]["results"]["quote"][1]["Ask"]
        dax = dataComm["query"]["results"]["quote"][2]["LastTradePriceOnly"]
        gold = dataComm["query"]["results"]["quote"][3]["Ask"]
        coil = dataComm["query"]["results"]["quote"][4]["Ask"]


        eur=dataCurr["query"]["results"]["rate"][0]["Rate"]
        jpy=dataCurr["query"]["results"]["rate"][1]["Rate"]
        cad=dataCurr["query"]["results"]["rate"][2]["Rate"]
        gpb=dataCurr["query"]["results"]["rate"][3]["Rate"]
        aud=dataCurr["query"]["results"]["rate"][4]["Rate"]
        nzd=dataCurr["query"]["results"]["rate"][5]["Rate"]
        chf=dataCurr["query"]["results"]["rate"][6]["Rate"]
        ils=dataCurr["query"]["results"]["rate"][7]["Rate"]


        mutex.acquire()
        try:
            timeDate = str(datetime.now())
            symbols = symbolGraphDB(SP = sp, NSD =nsd, DAX = dax, GOLD = gold, COIL = coil,EUR=eur,JPY=jpy,CAD=cad,GPB=gpb,AUD=aud,NZD=nzd,CHF=chf,ILS=ils,date=timeDate)
            symbols.put()
        finally:
            mutex.release()


app = webapp2.WSGIApplication([
    ('/cron', symbolGraph)
],debug=True)
