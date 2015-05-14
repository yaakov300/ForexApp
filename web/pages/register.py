__author__ = 'Oshri'

from google.appengine.ext.webapp import template
import webapp2

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

