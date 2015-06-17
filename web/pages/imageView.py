from google.appengine.ext import ndb
from models.historyDB import History
from google.appengine.ext.webapp import template

import cgi
import urllib
import webapp2

class imageView(webapp2.RequestHandler):
    def get(self):

        id = self.request.get('img_id')
        id = id[:-1]
        id = int(id)
        histories = History.getHistory()
        for h in histories:
            if id == h.key.id():
                id_img = h.key.urlsafe()

        #id = self.request.get('img_id')
        self.response.out.write('<html><body>')
        self.response.out.write('<div><img src="/img?img_id=%s"></img></div>' %id_img)
        self.response.out.write('</html></body>')

class Image(webapp2.RequestHandler):
    def get(self):
        img_key = ndb.Key(urlsafe=self.request.get('id_img'))
        image = img_key.get()
        if image.image:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(image.image)
        else:
            self.response.out.write('No image')
# [END image_handler]

app = webapp2.WSGIApplication([
    ('/imageView', imageView),
    ('/img', Image),
], debug=True)
