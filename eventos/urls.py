from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [    
    path('', views.index),
    path('about/', views.about),
    path('detalle/<codigo>/', views.detalle)
]
