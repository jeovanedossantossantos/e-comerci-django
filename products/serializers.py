from rest_framework import serializers
from products.models import Category
from users.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from rest_framework.response import Response

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description','user_id']

    def create(self, validated_data):
        return super(CategorySerializer, self).create(validated_data)