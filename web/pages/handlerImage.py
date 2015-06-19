import webapp2
from google.appengine.ext import ndb

class handlerImage(webapp2.RequestHandler):
    def get(self):
        img_key = ndb.Key(urlsafe=self.request.get('id_img'))
        imagePic = img_key.get()
        if imagePic.avatar:
            self.response.out.write('No image')
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(imagePic.avatar)
        else:
            self.response.out.write('No image')

app = webapp2.WSGIApplication([
    ('/handlerImage', handlerImage),
], debug=True)
