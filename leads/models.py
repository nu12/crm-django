from django.db import models

# Models: representation of database schema

class Lead(models.Model):
    SOURCE_CHOICES = (
        ('Youtube','Youtube'), # (DATABASE VALUE, DISPLAY VALUE)
        ('Google','Google'),
        ('Newsletter','Newsletter'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, blank=True, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)