from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_word/', views.check_word, name='check_word'),
]

