__author__ = 'idan'
from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User


class LoginHandler(webapp2.RequestHandler):
    def get(self):

        username = self.request.get('userName')
        password = self.request.get('password')

        user = User.query(User.username == username).get()
        if not user or not user.check_password(password):
            self.error(402)
            self.response.write('Wrong username or password')
            return

        self.response.set_cookie('our_token', str(user.key.id()))
        self.response.write(json.dumps({'status':'OK'}))

        template_params = {}
        html = template.render("web/templates/login.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/login', LoginHandler)
], debug=True)

