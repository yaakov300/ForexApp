__author__ = 'Oshri&Yaacov'
import webapp2
from google.appengine.ext.webapp import template
from models.historyDB import History

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        template_params['histories'] =[]
        histories = History.getHistory()
        for h in histories:
            template_params['histories'].append({
                "date": h.date,
                "symbol": h.symbol,
                "enterprice": h.enterprice,
                "stoplose": h.stoplose,
                "takeprofit": h.takeprofit,
                "profitorloss":h.profitorloss,
                "volume": h.volume,
                "lstype": h.lstype,
                "remarks": h.remarks
            })

        html = template.render("web/templates/history.html", template_params)
        self.response.write(html)

    def post(self):

        symboldb = self.request.get('symbol')
        enterPricedb = self.request.get('enterPrice')
        stopLosedb = self.request.get('stopLose')
        takeProfitdb = self.request.get('takeProfit')
        profitorlossdb = self.request.get('profitOrLoss')
        volumedb = self.request.get('volume')
        lstypedb = self.request.get('type')
        dateDB = self.request.get('date')
        remarksdb = self.request.get('remarks')
        history = History(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                      ,profitorloss = profitorlossdb,volume=volumedb, date=dateDB ,remarks = remarksdb,
                      lstype = lstypedb)

        history.put()
        self.redirect("/history")


app = webapp2.WSGIApplication([
    ('/history', HistoryHandler)
], debug=True)