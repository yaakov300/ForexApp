__author__ = 'idan'
from google.appengine.ext.webapp import template
from google.appengine.api import mail
import webapp2
from models.user import User



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
            template_params['error'] = '* Email address does not exist!'
            html = template.render("web/templates/forgetPass.html", template_params)
            self.response.write(html)

        else:

          sender_address ='jceforexapp@gmail.com'
          user_address = mail_forget
          print mail_forget
          subject = 'Forgot password or User Name?'
          username= user.username
          code = user.user_code
          code = str(code)

          body = 'Hello ' + username + '\n'+'Update new password here: http://youforrexapp.appspot.com/UpdatePass' + '\nUse this user code:' + code

          mail.send_mail(sender_address,user_address, subject, body)
          html = template.render("web/templates/login.html", template_params)
          self.response.write(html)


app = webapp2.WSGIApplication([
    ('/forgetPass', ForgetPassHandler)
], debug=True)