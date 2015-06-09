__author__ = 'idan'
from google.appengine.ext.webapp import template
from google.appengine.api import mail
import webapp2
from models.user import User
import hashlib
import json


class ForgetPassHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/forgetPass.html", template_params)
        self.response.write(html)


    def post(self):
        template_params = {}
        mail_forget = self.request.get("mailforget")
        user = User.query(User.mail == mail_forget).get()

        if not user:
            self.error(403)
            self.response.write('Email is not exists')
            return
        else:

          sender_address ='jceforexapp@gmail.com'
          user_address = mail_forget
          print mail_forget
          subject = 'Forgot password or User Name?'
          username= user.username
          body = 'hello ' + username + '\n'  +'Update new password: http://youforrexapp.appspot.com/UpdatePass'

          mail.send_mail(sender_address,user_address, subject, body)
          html = template.render("web/templates/login.html", template_params)
          self.response.write(html)


app = webapp2.WSGIApplication([
    ('/forgetPass', ForgetPassHandler)
], debug=True)