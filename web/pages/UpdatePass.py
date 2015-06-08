__author__ = 'idan'
from google.appengine.ext.webapp import template
from google.appengine.api import mail
import webapp2
from models.user import User
import hashlib
import json




class UpdatePassHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/UpdatePass.html", template_params)
        self.response.write(html)

    def post(self):
      username = self.request.get('userName')
      user = User.query(User.username == username).get()
      password = self.request.get('pwdup1')
      user.set_password(password)
      user.put
      self.redirect('/login')

app = webapp2.WSGIApplication([
    ('/UpdatePass', UpdatePassHandler)
], debug=True)