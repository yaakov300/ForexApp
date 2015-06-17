from google.appengine.ext import ndb
from models.historyDB import History
from google.appengine.ext.webapp import template
from models.user import User

import webapp2

class imageView(webapp2.RequestHandler):
    def get(self):
        id = self.request.get('id')
        self.response.out.write('<div><img src="/img?img_id=%s"></img>' %
                                    id)
        '''
        self.response.out.write('<div><img src="/img?img_id=%s"></img>' %
                                    History.img_key.image)'''


class Image(webapp2.RequestHandler):
    def get(self):
        img_key = ndb.Key(urlsafe=self.request.get('img_id')).get()
        image = img_key
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
