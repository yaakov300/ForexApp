__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2





class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/deletROW.html", template_params)
        self.response.write("hello world")


app = webapp2.WSGIApplication([
    ('/deletROW', DeleteHandler)
], debug=True)