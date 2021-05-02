from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Usage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=False)
    daytime = models.FloatField()
    nighttime = models.FloatField()