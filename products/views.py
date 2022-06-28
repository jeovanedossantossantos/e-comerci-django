import re
from django.conf import settings
from django.shortcuts import get_object_or_404, render


from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework import generics
from products.models import Category
from products.serializers import CategorySerializer
from users.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from users.middlewares import Middlewares
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
class CreateCategoryView(generics.CreateAPIView):
    def get_object(self,pk):
        
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get_object_category(self,pk):
        
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    def post(self, request):
        if('Authorization' in request.headers):
            print(request.headers)
            user_id=Middlewares.decode(request.headers)
            tipo = self.get_object(user_id)
            data = UserSerializer(tipo).data
            if(data["tipo"]=="admin"):
                data = request.data
                serializer = CategorySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
        return Response({'detail':"Não autorizado"})

    def get(self,request,id='', format=None):
       
        if(id==''):
            
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
          
        else:
            
            category = self.get_object_category(pk=id)
            serializer = CategorySerializer(category)

       
        return Response(serializer.data)

    def delete(self,request,id):
        if('Authorization' in request.headers):
            
            user_id=Middlewares.decode(request.headers)
            tipo = self.get_object(user_id)
            data = UserSerializer(tipo).data
            if(data["tipo"]=="admin"):
                category = self.get_object_category(pk=id)
                category.delete()
                serializer = CategorySerializer(category)
                if serializer.data:

                    return Response({'detail':"Excluido com sucesso."})
                else:
                    return Response({'detail':"Ouve um problema."})
        else:
            return Response({'detail':"Não autorizado"})
    
    def put(self, request, id):
        if('Authorization' in request.headers):
            
            user_id=Middlewares.decode(request.headers)
            tipo = self.get_object(user_id)
            data = UserSerializer(tipo).data
            if((user_id == id) or (data["tipo"]=="admin")):
                category = self.get_object_category(pk=id)
                serializer = CategorySerializer(category, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail':"Não autorizado"})
