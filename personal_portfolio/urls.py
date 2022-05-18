from django.contrib import admin
from django.urls import path
from personal_portfolio import views

urlpatterns = [
    path('',views.index, name="home"), 
    path('about',views.about, name="about"), 
    path('contact',views.contact, name="contact"), 
    path('resume',views.resume, name="resume"), 
    path('projects',views.projects, name="projects"), 
    
]