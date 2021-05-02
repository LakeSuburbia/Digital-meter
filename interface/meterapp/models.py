from django.db import models

class Usage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=False)
    daytime = models.FloatField()
    nighttime = models.FloatField()