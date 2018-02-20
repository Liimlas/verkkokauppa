from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_developer = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True, help_text="mm/dd/yyyy or yyyy-mm-dd")
    photo = models.ImageField(upload_to='user_pictures', default="", null=True, blank=True)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user, photo="")
        user_profile.save()
post_save.connect(create_profile, sender=User)



# Create your models here.
