from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.response import Response
# User = get_user_model()
# https://docs.djangoproject.com/en/4.0/ref/models/fields/
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    
    class Meta:
        model = User
        fields = ["id",'username', 'email', 'password',"tipo"]
    
    def create(self, validated_data):
        tipo = ['admin','user','client']
       
        if (validated_data['tipo'] not in tipo):
            validated_data['tipo'] = 'client'
        
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
       
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.save()
        return instance

