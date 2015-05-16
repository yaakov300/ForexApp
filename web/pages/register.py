from google.appengine.ext.webapp import template
import webapp2

from models.user import User

class RegisterHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
        html = template.render("web/templates/register.html", template_params)
        self.response.write(html)

    def post(self):
        uName = self.request.get('userName')
        pwd = self.request.get('password')
        ml = self.request.get('mail')
        self.user = User(userName=uName ,mail=ml,password=pwd)
        self.user.put()
        self.response.write(uName+pwd+ml)




app = webapp2.WSGIApplication([
    ('/register', RegisterHandler)
], debug=True)

