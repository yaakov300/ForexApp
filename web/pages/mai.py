from google.appengine.ext import webapp
import smtplib

import webapp2

class ParseXMLHandler(webapp2.RequestHandler):
    def get(self):

        from_addr    = 'jceforexapp@gmail.com'
        to_addr_list = ['yaacov300@gmail.com']
        cc_addr_list = ['yaacov300@gmail.com']
        subject      = 'Howdy'
        message      = 'Howdy from a python function aviram is slave!!!!'
        login        = 'jceforexapp'
        password     = 'YOUforex'
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

application = webapp.WSGIApplication([
    ('/cron', ParseXMLHandler)
],debug=True)




