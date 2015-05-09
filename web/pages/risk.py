__author__ = 'Oshri&Yaacov'

from google.appengine.ext.webapp import template
import webapp2

class RiskHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/risk.html", template_params)
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/risk', RiskHandler)
], debug=True)