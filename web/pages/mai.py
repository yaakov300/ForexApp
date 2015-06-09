from google.appengine.api import mail
import webapp2


class cronSendMail(webapp2.RequestHandler):
    def get(self):
        user_address = "jceforrexapp@gmail.com"
        senderadress = "aviram1202@gmail.com"
        name = "yaacov the king"
        comment = "temani is work"
       #mail.send_mail(senderadress, senderadress, "name: " + name + " mail: " + user_address , comment)

app = webapp2.WSGIApplication([
    ('/cron', cronSendMail)
],debug=True)
