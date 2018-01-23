from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)

    def terve(self):
        return "No tervepä terve!"