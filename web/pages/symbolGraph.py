import threading
from models.symbolGraphDB import symbolGraphDB
from threading import Lock
import json  #use for create json
from lib import requests   #Used for http requests
import webapp2
import logging


stComm="ESM15.CME,NQM15.CME,^GDAXI,GCM15.CMX,CLN15.NYM"
stCurr="EURUSD,JPYUSD,CADUSD,GBPUSD,AUDUSD,NZDUSD,CHFUSD,ILSUSD"
mutex = Lock()
class symbolGraph(webapp2.RequestHandler):

    def get(self):
        logging.info('from the get')
        self.threading_minuets()


    def threading_minuets(self):
        for i in range(12):
            t = threading.Timer(5*i, self.multiRequests)
            t.start()
            t.join()
        logging.info('end threading_minuets')


    #this function get all price for commodities and currency from yahoo api.
    def multiRequests(self):
        logging.info('from the multiRequests')

        URLComm="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+stComm+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
        URLCurr="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22"+stCurr+\
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
        logging.info('from the mutex')
        symbols = symbolGraphDB(SP = sp, NSD =nsd, DAX = dax, GOLD = gold, COIL = coil,EUR=eur,JPY=jpy,CAD=cad,GPB=gpb,AUD=aud,NZD=nzd,CHF=chf,ILS=ils)
        symbols.put()
        mutex.release()


app = webapp2.WSGIApplication([
    ('/cron', symbolGraph)
],debug=True)
