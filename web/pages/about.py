__author__ = 'Oshri&Yaacov'

from google.appengine.ext.webapp import template
import webapp2
from models.user import User

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username

        html = template.render("web/templates/about.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/about', AboutHandler)
], debug=True)