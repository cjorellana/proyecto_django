from django.shortcuts import render
from .models import Evento

# Create your views here.

def index(request):

    eventos = Evento.objects.all()

    data = {
        'titulo': "Principal",
        'listado': eventos
    }

    return render(request,"index.html",data)

def about(request):
    data = {
        'titulo': "About...",
        'contenido': "esta es la pagina de about"
    }
    return render(request,"about.html",data)