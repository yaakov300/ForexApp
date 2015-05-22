

from google.appengine.ext.webapp import template
from models.alertDB import Alert
import time
import webapp2

class AlertHandler(webapp2.RequestHandler):
    def get(self):

        template_params = {}

        template_params['alerts'] =[]
        alerts = Alert.getalerts()
        for a in alerts:
            template_params['alerts'].append({
                "date": a.date,
                "symbol": a.symbol,
                "enterprice": a.enterprice,
                "stoplose": a.stoplose,
                "takeprofit": a.takeprofit,
                "volume": a.volume
            })


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
        self.redirect("/alert")


app = webapp2.WSGIApplication([
    ('/alert', AlertHandler)
], debug=True)