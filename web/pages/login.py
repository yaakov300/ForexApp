__author__ = 'idan'
from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/login.html", template_params)
        self.response.write(html)


    def post(self):

        username = self.request.get('userName')
        password = self.request.get('pwd')

        user = User.query(User.username == username).get()

        if not user or not user.check_password(password):
            template_params = {}
            template_params['error'] = '* Wrong User Name or Password!'
            html = template.render("web/templates/login.html", template_params)
            self.response.write(html)
        else:
          self.response.set_cookie('our_token', str(user.key.id()))
          self.response.write(json.dumps({'status':'ok'}))
          self.redirect('/home')


app = webapp2.WSGIApplication([
    ('/login', LoginHandler)
], debug=True)

