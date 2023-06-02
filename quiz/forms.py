from dataclasses import field
import imp
from django.forms import ModelForm
from .models import Quiz, QuizInstance, Subject


class AnswerOptionsForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['options']
        labels = {
            'options': 'Choose Answer',
        }

class QuizInstanceForm(ModelForm):
    class Meta:
        model = QuizInstance
        fields = ['taker', 'quiz']  
        labels = {
            'taker': 'Name',
            'quiz': 'Subject'
        }      

class CreateSubjectForm(ModelForm):
    class Meta:
        model = Subject 
        fields = ['name', 'description', 'featured_image']
        labels = {
            'name': 'Subject',
        }       

class CreateQuestionForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['question', 'a', 'b', 'c', 'd', 'answer']