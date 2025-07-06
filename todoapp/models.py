from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    
