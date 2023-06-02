from django.urls import path
from . import views


urlpatterns = [
    path('signUp/', views.registerUser, name='sign-up'),
    path('signIn/', views.loginUser, name='sign-in'),
    path('logoutUser/', views.logoutUser, name='logout'),
]