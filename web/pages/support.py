__author__ = 'Oshri&Yaacov'

from google.appengine.api import mail
from google.appengine.ext.webapp import template


import webapp2

class SupportHandler(webapp2.RequestHandler):
    def get(self):
        template_params = {}
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