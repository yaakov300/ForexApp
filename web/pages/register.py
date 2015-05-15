__author__ = 'Oshri'

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb


import webapp2

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

    def post(self):

        userName = self.request.get("userName")
        password = self.request.get("password")
        confPass = self.request.get("confPass")
        mail = self.request.get("mail")




        self.response.out.write(userName+password+confPass+mail)

app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

