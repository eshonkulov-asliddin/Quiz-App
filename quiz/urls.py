from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('quiz-card/', views.quizCard, name='quiz-card'),
    path('question/<int:id>/', views.getQuestion, name='question'),
    path('result/<int:id>/', views.result, name='result'),
    path('retake/<int:id>/', views.retakeQuiz, name='retake'),
    path('create-quiz/', views.createQuiz, name='create-quiz'),
    path('create-question/<int:num>/<str:subject>', views.createQuestion, name='create-question'),
]
