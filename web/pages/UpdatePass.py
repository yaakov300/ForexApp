__author__ = 'idan'
from google.appengine.ext.webapp import template
from google.appengine.api import mail
import webapp2
from models.user import User
import hashlib
import json
import random



class UpdatePassHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/UpdatePass.html", template_params)
        self.response.write(html)

    def post(self):
      username = self.request.get('userName')
      code = self.request.get('code')
      code = int(code)
      newdbcode = random.randrange(1000,9999)

      user = User.query(User.username == username).get()
      if user:
         if user.user_code == code:
           password = self.request.get('pwdup1')
           user.set_password(password)
           user.set_user_code(newdbcode)
           self.redirect('/login')
         else:
            template_params = {}
            template_params['error'] = '* Wrong User Code!'
            html = template.render("web/templates/UpdatePass.html", template_params)
            self.response.write(html)
      else:
        template_params = {}
        template_params['error'] = '* Wrong User Name!'
        html = template.render("web/templates/UpdatePass.html", template_params)
        self.response.write(html)



app = webapp2.WSGIApplication([
    ('/UpdatePass', UpdatePassHandler)
], debug=True)