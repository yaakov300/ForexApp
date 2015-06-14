
from models.user import User
from google.appengine.ext.webapp import template
from models.alertDB import Alert
from models.symbolGraphDB import symbolGraphDB

import webapp2
import logging


class checkAlert(webapp2.RequestHandler):
    def get(self):
        logging.info("in croncheck")

        alerts = Alert.getalerts()
        for a in alerts:
            date= a.date
            symbol= a.symbol
            enterprice= a.enterprice
            stoplose=a.stoplose
            takeprofit= a.takeprofit
            volume= a.volume
            type=a.lstype
            username=a.username
            checkIfReached(symbol,enterprice,stoplose,takeprofit,type)

def checkIfReached(symbol,enPrice,stLoss,taPro,type):
    if (('/') in symbol):#is courrn
        stfrom=symbol[0:3]
        stTo=symbol[4:7]

        if (('USD') in stfrom):
            columArr=symbolGraphDB.getByCul(stTo)
        else:
            if (('USD') in stTo):
                columArr=symbolGraphDB.getByCul(stfrom)
            else:
                columArr=symbolGraphDB.getCurrCROS(stfrom,stTo)


    else:#is commditis
        columArr=symbolGraphDB.getByCul(symbol)

    for comm in columArr:
        if (type=="long"):
            if (comm>=taPro):
                logging.info('send mail god one '+symbol)
                break
            if(comm<=stLoss):
                logging.info('send mail - bad one-loss your cash'+symbol)
                logging.info(comm)
                logging.info(stLoss)
                logging.info(taPro)
                break
        else:#for short
            if (comm<=taPro):
                logging.info('send mail god one')
                break
            if (comm>=stLoss):
                logging.info('send mail - bad one-loss your cash')
                break





app = webapp2.WSGIApplication([
    ('/croncheck', checkAlert)
], debug=True)