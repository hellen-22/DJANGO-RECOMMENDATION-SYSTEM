from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    #path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    
]