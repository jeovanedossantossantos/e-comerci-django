from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

# default="user"
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#choices
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo=models.CharField(max_length=50)


