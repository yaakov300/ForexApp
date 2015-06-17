__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.alertDB import Alert
from models.user import User

import webapp2



class EditAlertHandler(webapp2.RequestHandler):

    def get(self):
        template_params = {}
        longType = True
        template_params['alerts'] =[]
        alerts = Alert.getalerts()

        id = self.request.get('id')
        id = id[:-1]
        id = int(id)



        for a in alerts:
            if id == a.key.id():
               editROW = a


        template_params['alerts'].append({

                "key": editROW.key.id(),
                "symbol": editROW.symbol,
                "enterprice": editROW.enterprice,
                "stoplose": editROW.stoplose,
                "takeprofit": editROW.takeprofit,
                "volume": editROW.volume,
                "lstype": editROW.lstype,
                "date": editROW.date

        })
        html = template.render("web/templates/editROWAL.html", template_params)
        self.response.write(html)

    def post(self):


        template_params = {}
        user = None



        id = self.request.get('id')
        id = id[:-1]
        id = int(id)


        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))
        dateDB = self.request.get('date')
        symboldb = self.request.get('symbol')
        enterPricedb = self.request.get('enterPrice')
        stopLosedb = self.request.get('stopLose')
        takeProfitdb = self.request.get('takeProfit')
        volumedb = self.request.get('volume')
        lstypeDB = self.request.get('typels')
        userDB = user.username
        alert = Alert(symbol=symboldb ,enterprice=enterPricedb,stoplose = stopLosedb,takeprofit=takeProfitdb
                      ,volume=volumedb , lstype = lstypeDB , username = userDB , date= dateDB)
        alert.put()

        alerts = Alert.getalerts()

        for a in alerts:

            if id == a.key.id():
               a.key.delete()
        self.redirect("/alert")

app = webapp2.WSGIApplication([
    ('/editROWAL', EditAlertHandler)
], debug=True)