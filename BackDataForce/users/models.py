from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    uniqueCode      =   models.CharField(max_length=200, blank=True, null=True) 
    name            =   models.CharField(max_length=200, blank=True, null=True) 
    generationDate  =   models.DateTimeField(auto_now_add=True) #models.DateField(blank=True, null=True)
    state            =   models.IntegerField(blank=True, null=True)
