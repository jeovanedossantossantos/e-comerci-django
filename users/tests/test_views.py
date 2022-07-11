from django.test import Client, RequestFactory
import pytest
from django.urls import resolve, reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
from users.models import User
from django.test import TestCase
from django.urls import reverse
# https://docs.djangoproject.com/en/4.0/topics/testing/overview/
# https://www.django-rest-framework.org/api-guide/testing/
# pytestmark = pytest.mark.django_db

from rest_framework.test import APITestCase

class TestListUsers(APITestCase):
    def setUp(self):
        self.admin = User.objects.create(
            username= "jeovagneggjj" ,
            email="jeovane@gmail.com",
            password= "123",
            tipo="admin"
        )
        self.admin.is_active = False
        self.admin.save()

       
      

    def test_list_users(self):
       
       
        response = self.client.get(
            f"/user/list/",
            
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        print(response_data)
       
        expected_data =[
            {
                "id": str(self.admin.id),
                "username": str(self.admin.username),
                "email": str(self.admin.email),
                "tipo": str(self.admin.tipo),
            }
         ]
      
        self.assertEqual(response_data, expected_data)
      
    def test_user(self):
       
       
        response = self.client.get(
            f"/user/public/"+str(self.admin.id)+"/",
            
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        
       
        expected_data ={
                "id": str(self.admin.id),
                "username": str(self.admin.username),
                "email": str(self.admin.email),
                "tipo": str(self.admin.tipo),
            }
         
       
        self.assertEqual(response_data, expected_data)

    def test_login(self):

        resp = self.client.post(f'/token/', {'username':"jeovagneggjj", 'password':"123"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        
   
       