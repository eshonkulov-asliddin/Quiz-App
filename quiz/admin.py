from django.contrib import admin
from .models import Subject, Quiz, QuizInstance

# Register your models here.
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(QuizInstance)