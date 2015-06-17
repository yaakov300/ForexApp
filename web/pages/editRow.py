__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2



class EditHandler(webapp2.RequestHandler):

    def get(self):
        template_params = {}
        longType = True
        template_params['histories'] =[]
        histories = History.getHistory()

        id = self.request.get('id')
        id = id[:-1]
        id = int(id)

        histories = History.getHistory()

        for h in histories:
            if id == h.key.id():
               editROW = h


        template_params['histories'].append({

                "key": editROW.key.id(),
                "date": editROW.date,
                "symbol": editROW.symbol,
                "enterprice": editROW.enterprice,
                "stoplose": editROW.stoplose,
                "takeprofit": editROW.takeprofit,
                "profitorloss":editROW.profitorloss,
                "volume": editROW.volume,
                "lstype": editROW.lstype,
                "remarks": editROW.remarks
        })
        html = template.render("web/templates/editRow.html", template_params)
        self.response.write(html)

    def post(self):


        template_params = {}
        user = None



        id = self.request.get('id')
        id = id[:-1]
        id = int(id)


        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        symboldb = self.request.get('symbol')
        enterPricedb = self.request.get('enterPrice')
        stopLosedb = self.request.get('stopLose')
        takeProfitdb = self.request.get('takeProfit')
        profitorlossdb = self.request.get('profitOrLoss')
        volumedb = self.request.get('volume')
        lstypedb = self.request.get('type')
        dateDB = self.request.get('date')
        remarksdb = self.request.get('remarks')
        userdb = user.username

        history = History(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                      ,profitorloss = profitorlossdb,volume=volumedb, date=dateDB ,remarks = remarksdb,
                      lstype = lstypedb, username = userdb)
        history.put()

        histories = History.getHistory()

        for h in histories:

            if id == h.key.id():
               h.key.delete()
        self.redirect("/history")

app = webapp2.WSGIApplication([
    ('/editROW', EditHandler)
], debug=True)