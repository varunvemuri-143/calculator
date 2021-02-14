from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about , name='about'),
    path("subjects", views.subjects, name='subjects'),
    path("contact", views.contact, name='contact'),
    path("financial", views.financial, name='financial'),
    path("math", views.math, name='math'),
    path("greetings", views.greetings, name='greetings'),
    path("physics", views.physics, name='physics'),
    path("basic_calculator",views.basic_calculator, name='basic_calculator'),
    path("distance",views.distance, name='distance'),
    path("velocity",views.velocity, name='velocity'),
    path("current",views.current, name='current'),
    path("equation",views.equation, name='equation'),
    path("escapevelocity",views.escapevelocity, name='escapevelocity'),
    path("force",views.force, name='force'),
    path("gravitationforce",views.gravitationforce, name='gravitationforce'),
    path("gravitationg",views.gravitationg, name='gravitationg'),
    path("kineticenergy",views.kineticenergy, name='kineticenergy'),
    path("potentialenergy",views.potentialenergy, name='potentialenergy'),
    

]