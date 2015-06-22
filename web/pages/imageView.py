#from google.appengine.ext import ndb
from models.historyDB import History
#from google.appengine.api import images
#from google.appengine.ext.webapp import template
import logging

#import cgi
#import urllib
import webapp2

class imageView(webapp2.RequestHandler):
    def get(self):

        id = self.request.get('img_id')
        id = id[:-1]
        id = int(id)
        histories = History.query()
        self.response.out.write('<html><body>')
        for h in histories:
            if id == h.key.id():
                self.response.out.write('<p>take one</p>')
                id_img = h.key.urlsafe()
                #id_img = h.key.id()
        self.response.out.write('<div><img src="/handlerImage?img_id=%s"></img></div>' %
                                   id_img)
        self.response.out.write('</html></body>')

app = webapp2.WSGIApplication([
    ('/imageView', imageView),
], debug=True)
