from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.
class Game(models.Model):
    name = models.CharField(blank=False, max_length=60,)
    developer = models.ForeignKey(User, blank=False)
    id = models.CharField(primary_key=True, max_length=50)
    price = models.FloatField(blank=False, validators=[MinValueValidator(0)])
    saleprice = models.FloatField(blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    onsale = models.BooleanField(blank=True)
    soldcopies = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0)])
    link = models.CharField(default='', blank=False, max_length=200)
    publish_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='game_pictures', default="")
    infotext = models.TextField(blank=True, max_length=500)
    ageRestriction = models.PositiveSmallIntegerField(blank=True, default=0)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

class BoughtGame(models.Model):
    owner = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    date = models.DateField(auto_now=True)

class HighScore(models.Model):
    scorer = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    score = models.FloatField(default=0)

class GameState(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(User)
    game_state = models.TextField(default="")
