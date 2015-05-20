__author__ = 'Oshri&Yaacov'

from google.appengine.ext.webapp import template
from models.alertDB import Alert
import time
import webapp2

class AlertHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/alert.html", template_params)
        self.response.write(html)

    def post(self):
        symboldb = self.request.get('symbol')
        enterPricedb = self.request.get('enterPrice')
        stopLosedb = self.request.get('stopLose')
        takeProfitdb = self.request.get('takeProfit')
        volumedb = self.request.get('volume')
        dateDB = time.strftime("%x")
        alert = Alert(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                      ,volume=volumedb, date=dateDB)
        alert.put()


app = webapp2.WSGIApplication([
    ('/alert', AlertHandler)
], debug=True)