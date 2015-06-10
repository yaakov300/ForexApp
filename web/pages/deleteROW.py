__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2





class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        id = self.request.get('id')

        #tmp1 = set(id.split(' '))

      # id.sub('\',0)
        id = id[:-1]
        id = int(id)

        histories = History.getHistory()

        for h in histories:


           # tmp2 = set(str(h.key.id()).split(' '))

            self.response.write(id)
            self.response.write('--')
            self.response.write(str(h.key.id()))
            self.response.write(',')
            #TODO - find the right condition

            if id == h.key.id():
               h.key.delete()


        self.redirect("/history")


app = webapp2.WSGIApplication([
    ('/deleteROW', DeleteHandler)
], debug=True)