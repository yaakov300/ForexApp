__author__ = 'Oshri&Yaacov'
from models.user import User
from google.appengine.ext.webapp import template
import webapp2


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username



        html = template.render("web/templates/home.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/home', HomeHandler)
], debug=True)

