from google.appengine.ext.webapp import template
import webapp2
import json
from models.user import User

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_variables = {}
        if user:
            template_variables['user'] = user.username

        html = template.render('templates/base.html', template_variables)
        self.response.write(html)



app = webapp2.WSGIApplication([
('/', MainHandler)
], debug=True)

