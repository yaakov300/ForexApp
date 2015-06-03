__author__ = 'Oshri&Yaacov'

from google.appengine.api import mail
from google.appengine.ext.webapp import template


import webapp2
from models.user import User
class SupportHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}

        user = None
        if self.request.cookies.get('our_token'):    #the cookie that should contain the access token!
            user = User.check_token(self.request.cookies.get('our_token'))

        template_params = {}
        if user:
            template_params['user'] = user.username


        html = template.render("web/templates/support.html", template_params)
        self.response.write(html)

    def post(self):
        template_params = {}
        user_address = self.request.get("mail")
        senderadress = "jceforexapp@gmail.com>"
        name = self.request.get("name")
        comment = self.request.get("comment")
        if not mail.is_email_valid(user_address):
            self.response.out.write("mail is wrong:"+ user_address+name+comment +senderadress)
        else:
            mail.send_mail(senderadress, senderadress, "name: " + name + " mail: " + user_address , comment)
            html = template.render("web/templates/Thankyou.html", template_params)
            self.response.write(html)


app = webapp2.WSGIApplication([
    ('/support', SupportHandler)
], debug=True)