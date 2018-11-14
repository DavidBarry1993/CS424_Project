from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True,null=True)
    
    
    
    #def link(k):
        #c=Player.objects.all()
        #u=User.objects.all()
        #for k in c:
            #for i in u:
                #if k.first_name == i.first_name
                #Player[k].user = u.i
                
    
    


class Club(models.Model):
    club_name = models.CharField(max_length=50)
    club_county = models.CharField(max_length=50)
    club_colours = models.CharField(max_length=50, null=True)
    
