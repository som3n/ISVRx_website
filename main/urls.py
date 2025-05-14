from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('training/', views.training, name='training'),
    path('join/', views.join, name='join'),
    path('contact/', views.contact, name='contact'),
]