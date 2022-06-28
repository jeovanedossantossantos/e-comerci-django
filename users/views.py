from django.conf import settings
from django.shortcuts import get_object_or_404, render


from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer
from users.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from .middlewares import Middlewares

class CreateUserView(generics.CreateAPIView):
    model = User

    permission_classes = [
        permissions.AllowAny
    ]
    

    serializer_class = UserSerializer
    

class UserViewsPrivate(APIView):
    permission_classes = (IsAuthenticated,)
   
    def get_object(self,pk):
        
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
  
    def delete(self, request, id, format=None):
        user_id=Middlewares.decode(request.headers)
        tipo = self.get_object(user_id)
        data = UserSerializer(tipo).data
        if((user_id == id) or (data["tipo"]=="admin")):
            

            user = self.get_object(id)
            user.delete()
            serializer = UserSerializer(user)
            if serializer.data:

                return Response({'detail':"Excluido com sucesso."})
        else:
            return Response({'detail':"Não autorizado"})

    def put(self, request, id, format=None):
        user_id=Middlewares.decode(request.headers)
        tipo = self.get_object(user_id)
        data = UserSerializer(tipo).data
        if((user_id == id) or (data["tipo"]=="admin")):
            messagem = 'Changed not password'
            user = self.get_object(id)
            userAnt = serializer = UserSerializer(user)
            data = request.data
        
            try:
            
                if(user.check_password(data['password_back'])):
                    user.set_password(data['password'])
                    messagem="Changed password"
            except:
                messagem = 'Changed not password'
                data['password'] = 'null'

            serializer = UserSerializer(user, data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"messagem":messagem})
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':"Não autorizado"})

class UserViewsPublic(APIView):
    
    def get_object(self,pk):
        
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404 
    def get(self, request, id, format=None):
        
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    class ListUsersView(generics.ListAPIView):
    
        def get(self, request, format=None):
            
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
           
            return Response(serializer.data)




    



   