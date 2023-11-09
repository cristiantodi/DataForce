from django.db import models
from users.models import User
# Create your models here.

class inventorey(models.Model):
    uniqueCode      =   models.CharField(max_length=200, blank=True, null=True) 
    generationDate  =   models.DateTimeField(auto_now_add=True) #models.DateField(blank=True, null=True)
    user            =   models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
    type            =   models.IntegerField(blank=True, null=True)
    model_id        =   models.CharField(max_length=200, blank=True, null=True)
    archive         =   models.FileField(upload_to='pdfs/') 