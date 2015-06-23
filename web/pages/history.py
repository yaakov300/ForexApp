
import sys
import webapp2
from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User
import logging

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

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
            if h.username != user.username:
                continue
            if h.avatar:
                template_params['histories'].append({
                    "key_urlsafe": h.key.urlsafe(),
                    "key": h.key.id(),
                    "date": h.date,
                    "symbol": h.symbol,
                    "enterprice": h.enterprice,
                    "stoplose": h.stoplose,
                    "takeprofit": h.takeprofit,
                    "profitorloss":h.profitorloss,
                    "volume": h.volume,
                    "lstype": h.lstype,
                    "remarks": h.remarks,
                    "img_src_url": "/handlerImage?img_id="+h.key.urlsafe()
                })
            else:
                template_params['histories'].append({
                    "key_urlsafe": h.key.urlsafe(),
                    "key": h.key.id(),
                    "date": h.date,
                    "symbol": h.symbol,
                    "enterprice": h.enterprice,
                    "stoplose": h.stoplose,
                    "takeprofit": h.takeprofit,
                    "profitorloss":h.profitorloss,
                    "volume": h.volume,
                    "lstype": h.lstype,
                    "remarks": h.remarks,
                    "img_src_url": "../static/images/no_image.png"
                })

          html = template.render("web/templates/history.html", template_params)
          self.response.write(html)


    def post(self):
        user = None
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
        imageDB = self.request.get('img')
        userdb = user.username

        sizeimage = sys.getsizeof(imageDB)
        if sizeimage<=1000000:   #size of image small from 1000000 byte
            try:
                history = History(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                              ,profitorloss = profitorlossdb,volume=volumedb, date=dateDB ,remarks = remarksdb,
                              lstype = lstypedb, username = userdb, avatar=imageDB)
            except:
                history = History(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                              ,profitorloss = profitorlossdb,volume=volumedb, date=dateDB ,remarks = remarksdb,
                              lstype = lstypedb, username = userdb)
            history.put()
            self.redirect("/history")
        else:
            template_params = {}
            template_params['ImageError'] = 'ERROR - your image is greater than 1MB'
            template_params['link'] = 'history'
            html = template.render("web/templates/error_page.html ", template_params)
            self.response.write(html)






app = webapp2.WSGIApplication([
    ('/history', HistoryHandler)
], debug=True)