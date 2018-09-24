import jwt
import datetime
from config import get_env
class user:
    def __init__(self, first_name, last_name, email, password, admin = False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.admin = admin

    def get_token(self):
        token = jwt.encode({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'admin': self.admin,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=get_env('AUTH_TOKEN_EXPIRY_DAYS'),
                                                                   seconds=get_env('AUTH_TOKEN_EXPIRY_SECONDS')),

        }, get_env('APP_SECRET'), algorithm='HS256')
        

    @staticmethod
    def decode(self, token):
        try:
            payload = jwt.decode(token, get_env['APP_SECRET'], algorithms='HS256')
            return payload['email']
        except jwt.ExpiredSignatureError:
            return 'signature expired'
        except jwt.InvalidTokenError:
            return 'Invalid Token'
