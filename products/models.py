from django.db import models
from uuid import uuid4

from users.models import User

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
    #     db_table = 'categories'

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
    #     db_table = 'products'