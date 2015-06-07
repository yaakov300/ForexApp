__author__ = 'valerybo'


from google.appengine.ext.webapp import template
from models.historyDB import History
from models.user import User

import webapp2





class DeleteHandler(webapp2.RequestHandler):


     def delete(self,key):
         tmp = ndb.get(key)
         tmp.delete()
         self.redirect("/history")


    app = webapp2.WSGIApplication([
    ('/deleteROW', DeleteHandler)
], debug=True)