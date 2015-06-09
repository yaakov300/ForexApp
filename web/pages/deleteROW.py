__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2





class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        id = self.request.get('id')
        self.response.write(id)
        histories = History.getHistory()

        for h in histories:
            self.response.write(h.key)
            if h.key == id:
                h.delete
                self.response.write('a')


       # self.redirect("/history")


app = webapp2.WSGIApplication([
    ('/deleteROW', DeleteHandler)
], debug=True)