
from models.user import User
from google.appengine.ext.webapp import template
from models.alertDB import Alert
from models.symbolGraphDB import symbolGraphDB
import webapp2
import logging


class checkAlert(webapp2.RequestHandler):
    def get(self):
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

def checkIfReached(self,symbol,enPrice,stLoss,taPro,type):
    symbolGraph=symbolGraphDB.getsSymbolGraph()
    '''
    if (symbol.find("/")==0):#is courrn
        stfrom=symbol[0:3]
        stTo=symbol[4:7]
        #if ((stfrom.find("USD"))|(stTo.find("USD"))):
    else:#is commditis
    '''
    for comm in symbolGraph:
        sp=comm.SP
        if (type=="long"):
            if (sp>taPro):
                logging.info('send mail god one')
            if(sp<stLoss):
                logging.info('send mail - bad one-loss your cash')
        else:#for short
            if (sp<taPro):
                logging.info('send mail god one')
            if (sp>stLoss):
                logging.info('send mail - bad one-loss your cash')
















app = webapp2.WSGIApplication([
    ('/alert', checkAlert)
], debug=True)