from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    phone=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=200 , null=True , blank=True)

#def save_profile_user(sender,**kwargs):
   # if kwargs['created']:
    #    profile_user=profile(user=kwargs['instance'])
     #   profile_user.save()


#post_save.connect(save_profile_user,sender=User)