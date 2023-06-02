
from django.db import models
from django.contrib.auth.models import User

from quiz.models import Quiz
from quiz.models import Subject


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    programming_language = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    completed_subject = models.ManyToManyField(Subject, default=Subject.objects.all)
   

    

    def __str__(self) -> str:
        return str(self.username)
