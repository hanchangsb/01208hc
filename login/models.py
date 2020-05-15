from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    age = models.IntegerField()
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    enable = models.BooleanField(default=True)
