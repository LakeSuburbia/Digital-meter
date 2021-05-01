from django.db import models

# Create your models here.
class Usage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=False)
    daytime = models.FloatField()
    nighttime = models.FloatField()
