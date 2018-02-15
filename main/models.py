from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(blank=False, max_length=60, validators=[RegexValidator(regex='^.{3}$', message='The name has to be atleast 3 characters long!', code='nomatch')])
    developer = models.ForeignKey(User, blank=False)
    id = models.CharField(primary_key=True, max_length=50)
    price = models.FloatField(blank=False, validators=[MinValueValidator(0)], help_text='Price of the game')
    saleprice = models.FloatField(blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    onsale = models.BooleanField(blank=True)
    soldcopies = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])



