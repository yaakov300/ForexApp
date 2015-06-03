__author__ = 'Oshri&Yaacov'

from google.appengine.ext.webapp import template
import webapp2
from models.user import User
class RiskHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username

        if not user:
            self.redirect('/home')

        html = template.render("web/templates/risk.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/risk', RiskHandler)
], debug=True)