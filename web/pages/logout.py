__author__ = 'idan'
import webapp2

class LogoutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.delete_cookie('our_token')
        self.redirect('/')
