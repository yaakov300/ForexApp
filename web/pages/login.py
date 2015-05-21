__author__ = 'idan'
from google.appengine.ext.webapp import template
import webapp2

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/login.html", template_params)
        self.response.write(html)






app = webapp2.WSGIApplication([
    ('/login', HomeHandler)
], debug=True)

