from google.appengine.ext import ndb
import hashlib      #we need this to safely store passwords
import logging


class User(ndb.Model):
    username = ndb.StringProperty()
    mail = ndb.StringProperty()
    password = ndb.StringProperty()
    user_code = ndb.IntegerProperty()

    @staticmethod
    def check_token(token):
        user = User.get_by_id(long(token))
        return user

    def set_password(self, password):
        self.password = hashlib.md5(password).hexdigest()
        self.put()

    def set_user_code(self,code):
        self.user_code=code
        self.put

    def check_password(self, password):
        if not password:
            return False
        logging.info("self.pass: {}, hashed pass: {}".format(self.password, hashlib.md5(password).hexdigest()))
        if self.password == hashlib.md5(password).hexdigest():
            return True

        return False