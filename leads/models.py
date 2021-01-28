from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # Need to specify custom User model in settings.py
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # on_delete: CASCADE, SET_NULL, SET_DEFAULT
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Using the manager
# Lead.objects.create(first_name = 'A', last_name = 'B', age = 30)
# Lead.objects.all()
# Lead.objects.filter(first_name='A')
# Lead.objects.filter(age__gt= 20)
# Lead.objects.get(id=15)