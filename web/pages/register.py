from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User
import random

class RegisterHandler(webapp2.RequestHandler):
    def get(self):

        template_params = {}
        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

    def post(self):
            template_params = {}
            flag_error =False
            maildb = self.request.get('mail')
            passworddb = self.request.get('pwd1')
            usernamedb = self.request.get('userName')
            usercode = random.randrange(1000,9999)

            user = User.query(User.username == usernamedb).get()
            if user:
                template_params['error_userName'] = '* User Name is already exists!'
                flag_error = True

            user = User.query(User.mail == maildb).get()
            if user:
                template_params['error_mail'] = '* Mail is already exists!'
                flag_error = True

            if flag_error == True:
                html = template.render("web/templates/register.html", template_params)
                self.response.write(html)
                return
            else:
               user = User(username=usernamedb, mail=maildb,user_code=usercode)
               user.set_password(passworddb)
               user.put()

               self.response.set_cookie('our_token', str(user.key.id()))
               self.response.write(json.dumps({'status':'OK'}))
               self.redirect("/home")

app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

