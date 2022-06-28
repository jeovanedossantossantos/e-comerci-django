from django.test import RequestFactory
import pytest
from django.urls import resolve, reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
from users.models import User
from django.test import TestCase
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

        self.admin.save()

    def test_list_users(self):
        login = self.client.force_authenticate(user=self.admin)
       
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
        print(expected_data)
        self.assertEqual(response_data, expected_data)
      

    

class TestDetailUsers():
    pass

