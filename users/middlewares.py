from django.conf import settings
import jwt

class Middlewares():

    def decode(tokem):
        if("Bearer" in tokem.get('Authorization')):
            des = jwt.decode(tokem.get('Authorization').split(' ')[1],settings.SECRET_KEY, algorithms=['HS256'])
        else:
            des = jwt.decode(tokem.get('Authorization'),settings.SECRET_KEY, algorithms=['HS256'])

        return des["user_id"]

