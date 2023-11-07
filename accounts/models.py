from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    pass
app_name = 'accounts'

class CustomUser(AbstractUser):
    # Define additional fields
    id = models.AutoField(primary_key=True)
    permission = models.CharField(max_length=100,default="일반")
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    objects = CustomUserManager()
   
    class Meta:
        swappable = 'accounts.CustomUser'


   