from django.db import models
from users.models import User

# Create your models here.

class analizys(models.Model):
    uniqueCode  =   models.CharField(max_length=200, blank=True, null=True) 
    user        =   models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    initiated   =   models.DateField(blank=True, null=True)
    termination =   models.DateField(blank=True, null=True)
    result      =   models.IntegerField(blank=True, null=True)
    type        =   models.IntegerField(blank=True, null=True)  

