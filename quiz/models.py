from enum import unique
from django.db import models
from django.contrib.auth.models import User



ANSWER_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
)

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)  


    class Meta:
        ordering = ['id']     


class Quiz(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(null=True, blank=True)
    a = models.CharField(max_length=50, null=True, blank=True, unique=True)
    b = models.CharField(max_length=50, null=True, blank=True, unique=True)
    c = models.CharField(max_length=50, null=True, blank=True, unique=True)
    d = models.CharField(max_length=50, null=True, blank=True, unique=True)
    options = models.CharField(max_length=50, choices=ANSWER_CHOICES,  blank=True, null=True, default='A')
    answer = models.CharField(max_length=50, blank=True, null=True)
    submitted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.question)

    class Meta:
        ordering = ['question']       



class QuizInstance(models.Model):   
    taker = models.CharField(max_length=200, null=True, blank=True)
    quiz = models.CharField(null=True, blank=True, max_length=200)  
    quiz_taken = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)
    complete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.taker)

 