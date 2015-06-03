from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import smtplib


class ParseXMLHandler(webapp.RequestHandler):
    def get(self):

        from_addr    = 'jceforexapp@gmail.com'
        to_addr_list = ['aviram1202@gmail.com']
        cc_addr_list = ['aviram1202@gmail.com']
        subject      = 'Howdy'
        message      = 'Howdy from a python function aviram is king!!!!'
        login        = 'jceforexapp'
        password     = 'YOUfor ex'
        sendemail(from_addr,to_addr_list,cc_addr_list,subject,message,login,password)

    def sendemail(from_addr, to_addr_list,cc_addr_list,subject, message,login, password,smtpserver='smtp.gmail.com:587'):
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login,password)
        problems = server.sendmail(from_addr, to_addr_list, message)
        server.quit()


application = webapp.WSGIApplication([('/mail', ParseXMLHandler)],debug=True)




