from django.db import models

# Create your models here.
class Usage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=False)
    daytime = models.FloatField()
    nighttime = models.FloatField()
    #datacontainer = models.ForeignKey('Data', on_delete=models.CASCADE)

#class Data(models.Model):
    #updatetime = models.DateTimeField(auto_now_add=True)