__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.alertDB import Alert
from models.user import User

import webapp2





class DeleteAlertHandler(webapp2.RequestHandler):
    def get(self):

        template_params = {}

        id = self.request.get('id')
        id = id[:-1]
        id = int(id)

        alerts = Alert.getalerts()

        for a in alerts:

            self.response.write(id)
            self.response.write('--')
            self.response.write(str(a.key.id()))
            self.response.write(',')
            #TODO - find the right condition

            if id == a.key.id():
                a.key.delete()


        self.redirect("/alert")


app = webapp2.WSGIApplication([
    ('/deleteROWAL', DeleteAlertHandler)
], debug=True)

