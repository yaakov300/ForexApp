import webapp2
from google.appengine.ext import ndb
import cgi
import urllib
from models.historyDB import History
import logging

from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.api import users
from models.historyDB import History

class handlerImage(webapp2.RequestHandler):
    def get(self):
        img_id= self.request.get('img_id')
        img_key = ndb.Key(urlsafe=img_id)
        imagePic = img_key.get()
        if imagePic.avatar:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(imagePic.avatar)
        else:
            self.response.out.write('No image')

app = webapp2.WSGIApplication([
    ('/handlerImage', handlerImage),
], debug=True)
