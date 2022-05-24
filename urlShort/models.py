from datetime import datetime
from django.db import models
from datetime import datetime

# Create your models here.
class Url_User(models.Model):
    user_id = models.IntegerField(null=True,blank=True)

class Url_Model(models.Model):
    longurl = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=5)
    campaign_id = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(Url_User,on_delete=models.CASCADE)


class url_analytics(models.Model):
    url = models.ForeignKey(Url_Model,on_delete=models.CASCADE)
    dlr_id = models.IntegerField(blank=True,null=True)
    count = models.IntegerField(default=0)
    ip_address = models.CharField(max_length=32,blank=True,null=True)
    location = models.CharField(max_length=500,blank=True,null=True)
    date = models.DateTimeField(default=datetime.now())
    
    
    
