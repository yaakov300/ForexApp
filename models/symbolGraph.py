import threading
from models.symbolGraphDB import symbolGraphDB
from threading import Lock
import json  #use for create json
import requests  #Used for http requests
import webapp2
import logging

mutex = Lock()
class symbolGraph(webapp2.RequestHandler):
    def get(self):
        logging.info('from the cron')
        self.threading_minuets()
        #self.multiRequests()

    def threading_minuets(self):
        for i in range(10):
            threading.Timer(1*i, self.multiRequests).start()


    #this function get all price for commodities and currency from yahoo api.
    def multiRequests(self):
        logging.info('from the thread')
        '''
        with open('../web/static/json/symbols.json') as data_file:
            data = json.load(data_file)
        '''


        stComm="ESU15.CME,NQU15.CME,GDAXI,GCQ15.CMX,CLQ15.NYM"
        stCurr=""
        stDax=""
        line=0;
        '''
        for i in data["symbol"]:
            if (line<5):
                stComm=stComm+''+i["symbolName"]+','
            else:
                stCurr=stCurr+''+i["symbolName"]+','
            line=line+1
        stComm=stComm[:-1]
        stCurr=stCurr[:-1]
        '''
        URLComm="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+stComm+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="

        '''
        stCurr="EURUSD"
        URLCurr="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22"+stCurr+\
            "%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="
        '''

        requestComm = self.requests.get(URLComm)
        dataComm = requestComm.json()#["query"]["results"]["quote"]["Ask"]
        '''
        requestCurr = requests.get(URLCurr)
        dataCurr = requestCurr.json()#["query"]["results"]["rate"]["Rate"]
        '''

        mutex.acquire()
        sp = dataComm["query"]["results"]["quote"][0]["Ask"]
        nsd = dataComm["query"]["results"]["quote"][1]["Ask"]
        dax = dataComm["query"]["results"]["quote"][2]["LastTradePriceOnly"]
        gold = dataComm["query"]["results"]["quote"][3]["Ask"]
        coil = dataComm["query"]["results"]["quote"][4]["Ask"]
        symbols = symbolGraphDB(SP = sp, NSD =nsd, DAX = dax, GOLD = gold, COIL = coil)
        symbols.put()
        try:
            #print all Commodities
            '''
            for i in range(dataComm["query"]["count"]):
                if (i!=2):
                        #print (dataComm["query"]["results"]["quote"][i]["Ask"])
                    arrPrice.append(dataComm["query"]["results"]["quote"][i]["Ask"])
                else:#for Dax
                    #print (dataComm["query"]["results"]["quote"][i]["LastTradePriceOnly"])
                    arrPrice.append(dataComm["query"]["results"]["quote"][i]["LastTradePriceOnly"])
            #print all Currency
            for i in range(dataCurr["query"]["count"]):
                #print (dataCurr["query"]["results"]["rate"][i]["Rate"])
                arrPrice.append(dataCurr["query"]["results"]["rate"][i]["Rate"])
            '''
            price=dataCurr["query"]["results"]["rate"]["Rate"]
           # print("arr start")
            symbolGraph.price = price
            symbolGraph.put()
        finally:
            mutex.release()



app = webapp2.WSGIApplication([
    ('/cron', symbolGraph)
],debug=True)
