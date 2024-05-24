# userform--2063
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class ExtraInfo(AbstractBaseUser):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    profile_pic = models.ImageField(upload_to='images/')
    phone_number = models.CharField(max_length=50, unique=True)
    USER_GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )
    gender = models.CharField(max_length=20, choices=USER_GENDER_CHOICES)
    USER_COUNTRY_CHOICES = (
        ('India', 'India'),
        ('USA', 'USA'),
        ('Canada', 'Canada'),
    )
    country = models.CharField(max_length=20, choices=USER_COUNTRY_CHOICES)
    hobbies = models.CharField(max_length=255)
