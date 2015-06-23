

from google.appengine.api import mail
from google.appengine.ext.webapp import template


import webapp2
from models.user import User
class error_pageHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username

        template_params['ImageError'] = 'ERROR - your image is greater than 1MB'
        template_params['link'] = 'history'
        html = template.render("web/templates/error_page.html", template_params)
        self.response.write(html)


app = webapp2.WSGIApplication([
    ('/error_page', error_pageHandler)
], debug=True)