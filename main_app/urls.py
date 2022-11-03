from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('headphones/', views.headphones_index, name='headphones_index'),
]