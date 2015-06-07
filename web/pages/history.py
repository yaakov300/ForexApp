__author__ = 'Oshri&Yaacov'
import webapp2
from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User


class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username

        if not user:
             template_params['noaccess'] = 'PURCHEASE HISTORY'
             html = template.render("web/templates/home.html", template_params)
             self.response.write(html)

        else:
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
        avatardb = self.request.get('snapShot')
        history = History(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                      ,profitorloss = profitorlossdb,volume=volumedb, date=dateDB ,remarks = remarksdb,
                      lstype = lstypedb,avatar = avatardb)
        history.put()
        self.redirect("/history")


app = webapp2.WSGIApplication([
    ('/history', HistoryHandler)
], debug=True)