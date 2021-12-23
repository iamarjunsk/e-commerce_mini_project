from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shop(models.Model):
    user = models.ForeignKey(User,related_name='shops',on_delete=models.CASCADE)
    shopname = models.CharField(max_length=255)
    addreess = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.shopname