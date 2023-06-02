from audioop import add
from urllib import request
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserAccount
from quiz.models import Subject


subjects = Subject.objects.all()
    


def CreateProfile(sender, created, instance, **kwargs):
    subjects = Subject.objects.all()
    if created:
        user = instance
        profile = UserAccount.objects.create(
            user = user,
            username=user.username,
            email=user.email,
        )

def DeleteProfile(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()                
    except:
        pass

post_save.connect(CreateProfile, sender=User) 
post_delete.connect(DeleteProfile, sender=UserAccount)
