from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User


class RegisterHandler(webapp2.RequestHandler):
    def get(self):

        template_params = {}
        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

    def post(self):

            maildb = self.request.get('mail')
            passworddb = self.request.get('pwd1')
            usernamedb = self.request.get('userName')

            user = User.query(User.username == usernamedb).get()
            if user:
                  self.error(403)
                  self.response.write('username is already exists ')
                  return

            user = User.query(User.mail == maildb).get()
            if user:
                self.error(403)
                self.response.write('Email is already exists ')
                return

            user = User(username=usernamedb, mail=maildb)
            user.set_password(passworddb)
            user.put()

            self.response.set_cookie('our_token', str(user.key.id()))
            self.response.write(json.dumps({'status':'OK'}))

            self.redirect("/home")

app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

