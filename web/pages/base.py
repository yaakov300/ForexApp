from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username

        html = template.render('web/templates/home.html', template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
('/', MainHandler)
], debug=True)

