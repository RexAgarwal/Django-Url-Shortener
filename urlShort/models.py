from django.db import models


# Create your models here.

class urlModel(models.Model):
    longurl = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=5)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.shorturl
