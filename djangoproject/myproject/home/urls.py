from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path('contact', views.contact, name='contact'),
    path("service", views.service, name="service"),
    path('about', views.about, name='about')
]   
