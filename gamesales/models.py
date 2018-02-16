from django.db import models

# Create your models here.


class AddGame(models.Model):
  description = models.CharField(max_length=255, blank=True)
  developer = models.CharField(blank=True, max_length=100)
  title = models.CharField(max_length=100, blank=True)
  price = models.CharField(null=True, blank=True, max_length=5)
   # uploaded_at = models.DateTimeField(auto_now_add=True)



