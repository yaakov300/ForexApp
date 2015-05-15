__author__ = 'Oshri'

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.user import User

import webapp2

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

    def post(self):


        confPass = self.request.get("confPass")

        User(userName = self.request.get("userName") ,
             password = self.request.get("password"),
             mail = self.request.get("mail"))



app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

