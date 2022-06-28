from django.conf import settings
import jwt

class Middlewares():

    def decode(tokem):
        des = jwt.decode(tokem.get('Authorization').split(' ')[1],settings.SECRET_KEY, algorithms=['HS256'])
        
        return des["user_id"]