from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
class Product(models.Model):
    title=models.CharField(max_length=20)
    date= models.DateTimeField(default=datetime.now)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active= models.BooleanField(default= True)
    content=models.TextField()
    def __str__(self):
        return self.title
    
# Create your models here.
