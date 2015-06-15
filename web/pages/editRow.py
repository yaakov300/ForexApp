__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2



class EditHandler(webapp2.RequestHandler):

    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        if user:
            template_params['user'] = user.username


        template_params['histories'] =[]
        histories = History.getHistory()

        id = self.request.get('id')
        id = id[:-1]
        id = int(id)

        histories = History.getHistory()

        for h in histories:

            self.response.write(id)
            self.response.write('--')
            self.response.write(str(h.key.id()))
            self.response.write(',')
            #TODO - find the right condition

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
        html = template.render("web/templates/editROW.html", template_params)
        self.response.write(html)

        #self.redirect("/history")

app = webapp2.WSGIApplication([
    ('/editROW', EditHandler)
], debug=True)