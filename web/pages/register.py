from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User


class RegisterHandler(webapp2.RequestHandler):
    def get(self):

        template_params = {}

        email = self.request.get('mail')
        password = self.request.get('password')
        user_name = self.request.get('userName')
        first_name = self.request.get('firstName')
        last_name = self.request.get('lastName')

        user = User.query(User.username == user_name).get()

        if user:
                self.error(402)
                self.response.write('user name is already in system')
                return
        user = User.query(User.mail == email).get()

        if user:
                self.error(402)
                self.response.write('Email is already in system')
                return

        user = User()
        user.mail = email
        user.username = user_name
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.put()

        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

        self.response.set_cookie('our_token', str(user.key.id()))
        self.response.write(json.dumps({'status':'OK'}))

app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

