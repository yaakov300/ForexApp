import threading
from models.symbolGraphDB import symbolGraphDB
from models.alertDB import Alert
from models.user import User
from google.appengine.api import mail

from lib import requests   #Used for http requests
import webapp2
import logging
from datetime import datetime
from threading import Lock

stComm="ESU15.CME,NQU15.CME,GDAXI,GCQ15.CMX,CLQ15.NYM"

stCurr="EURUSD,JPYUSD,CADUSD,GBPUSD,AUDUSD,NZDUSD,CHFUSD,ILSUSD"
mutex = Lock()
class symbolGraph(webapp2.RequestHandler):

    def get(self):
        logging.info('from the get')
        self.threading_minuets()

    def threading_minuets(self):
        threadArr = []

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
        #check if alerts in not empty
        exists = Alert.getalerts().get()
        if exists is None: #alerts it's not empty!
            return
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
        try:
            timeDate = str(datetime.now())
            #symbols = symbolGraphDB(SP = sp, NSD =nsd, DAX = dax, GOLD = gold, COIL = coil,EUR=eur,JPY=jpy,CAD=cad,GPB=gpb,AUD=aud,NZD=nzd,CHF=chf,ILS=ils,date=timeDate)
            symbolToCheck = {'minSP': sp, 'NSDQ': nsd, 'DAX': dax, 'GOLD': gold, 'C.OIL': coil, 'EUR': eur, 'JPY': jpy, 'CAD': cad, 'GPB': gpb, 'AUD': aud, 'NZD': nzd, 'CHF': chf, 'ILS': ils}

            for symbol in symbolToCheck:
                try:
                    symbolToCheck[symbol] = float(symbolToCheck[symbol])
                except ValueError:
                    logging.info(symbol)
            #symbols.put()
        finally:
            mutex.release()
        checkAlert(symbolToCheck)


def checkAlert(symbolToCheck):
    alerts = Alert.getalerts()
    for a in alerts:
        date= a.date
        symbol= a.symbol
        enterprice= float(a.enterprice)
        stoplose= float(a.stoplose)
        takeprofit= float(a.takeprofit)
        volume= a.volume
        type=a.lstype
        username=a.username
        alert = checkIfReached(username,symbol,enterprice,stoplose,takeprofit,type,volume,symbolToCheck)
        if (alert == 'send'):
            a.key.delete()


def checkIfReached(username,symbol,enPrice,stLoss,taPro,type,volume,symbolToCheck):
    userMail = getEmailByUserName(username)
    arrayMail = {'username': username, 'symbol': symbol, 'enPrice': enPrice, 'stLoss': stLoss, 'taPro': taPro, 'type': type, 'volume': volume, 'userMail': userMail}
    good ="good"
    bad = "bad"



    if (('/') in symbol):#is courrnet
        stfrom=symbol[0:3]
        stTo=symbol[4:7]
        if (('USD') in stfrom): #USD/***
            if (type=="long"):
                if (1/symbolToCheck[stTo]>=taPro):
                    sendMailAlert(arrayMail,good)
                    return 'send'
                if(1/symbolToCheck[stTo]<=stLoss):
                    sendMailAlert(arrayMail,bad)
                    return 'send'
                else:#for short
                    if (1/symbolToCheck[stTo]<=taPro):
                        sendMailAlert(arrayMail,good)
                        return 'send'
                    if (1/symbolToCheck[stTo]>=stLoss):
                        sendMailAlert(arrayMail,bad)
                        return 'send'
        else:
            if (('USD') in stTo): #***/USD
                if (type=="long"):
                    if (symbolToCheck[stfrom]>=taPro):
                         sendMailAlert(arrayMail,good)
                         return 'send'
                    if(symbolToCheck[stfrom]<=stLoss):
                        sendMailAlert(arrayMail,bad)
                        return 'send'
                else:#for short
                    if (symbolToCheck[stfrom]<=taPro):
                        sendMailAlert(arrayMail,good)
                        return 'send'
                    if (symbolToCheck[stfrom]>=stLoss):
                        sendMailAlert(arrayMail,bad)
                        return 'send'
            else:   #***/***
                if (type=="long"):
                    if (symbolToCheck[stfrom]/symbolToCheck[stTo]>=taPro):
                        sendMailAlert(arrayMail,good)
                        return 'send'
                    if(symbolToCheck[stfrom]/symbolToCheck[stTo]<=stLoss):
                        sendMailAlert(arrayMail,bad)
                        return 'send'
                else:#for short
                    if (symbolToCheck[stfrom]/symbolToCheck[stTo]<=taPro):
                        sendMailAlert(arrayMail,good)
                        return 'send'
                    if (symbolToCheck[stfrom]/symbolToCheck[stTo]>=stLoss):
                        sendMailAlert(arrayMail,bad)
                        return 'send'
    else:#is commditis
        if (type=="long"):
            if (symbolToCheck[symbol]>=taPro):
                    sendMailAlert(arrayMail,good)
                    return 'send'
            if(symbolToCheck[symbol]<=stLoss):
                    sendMailAlert(arrayMail,bad)
                    return 'send'
        else:#for short
            if (symbolToCheck[symbol]<=taPro):
                sendMailAlert(arrayMail,good)
                return 'send'
            if (symbolToCheck[symbol]>=stLoss):
                sendMailAlert(arrayMail,bad)
                return 'send'
    return 'not send'

def getEmailByUserName(userName):
    users = User.getUser()
    for u in users:
        if (u.username == userName):
            return u.mail
    return "no user"

def sendMailAlert(arrayMail,pofitOrLoss):

     user_address = "jceforexapp@gmail.com"
     senderadress = arrayMail['userMail']
     name = "ForexApp-Alert"
     comment = "Hello " + arrayMail['username'] + "\n\n"
     if(pofitOrLoss == "good"): #transaction was completed successfully
        comment = comment + "Your transaction has been completed successfully" + "\n"
     else:#transaction was failed
        comment = comment + "Your transaction has been failed" + "\n"
     comment = comment + "\tsymbol:" + arrayMail['symbol'] + "\n" +\
        "\tType: " + str(arrayMail['type']) + "\n" +\
        "\tEnter Price: " + str(arrayMail['enPrice']) + "\n" +\
        "\tTake Profit: " + str(arrayMail['taPro']) + "\n" +\
        "\tStop Loss: " + str(arrayMail['stLoss']) + "\n" +\
        "\tVolume: " + str(arrayMail['volume']) + "\n\n" +\
        "Thank you!\n  ForexApp"
     mail.send_mail(user_address, senderadress,  name , comment)




app = webapp2.WSGIApplication([
    ('/cron', symbolGraph)
],debug=True)
