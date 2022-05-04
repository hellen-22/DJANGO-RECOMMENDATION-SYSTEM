from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('home/', views.home, name='home'),
]