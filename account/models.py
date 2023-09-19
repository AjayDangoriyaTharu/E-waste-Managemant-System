from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


# class contectEnquiry(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=60)
#     phone = models.CharField(max_length=50)
#     Address = models.CharField(max_length=200)
#     objects = models.CharField(max_length=50)
#     object_description = models.TextField()


# ()
