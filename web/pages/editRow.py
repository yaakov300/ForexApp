__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2



class EditHandler(webapp2.RequestHandler):
    def get(self):

        template_params = {}

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

          #  if id == h.key.id():
        #       h.key.delete()


       # self.redirect("/alert")


app = webapp2.WSGIApplication([
    ('/editROW', EditHandler)
], debug=True)