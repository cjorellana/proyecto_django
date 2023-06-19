from django.shortcuts import render,get_object_or_404
from .models import Evento


# Create your views here.

def index(request):

    eventos = Evento.objects.all()

    data = {
        'titulo': "Principal",
        'listado': eventos
    }

    return render(request,"index.html",data)

def detalle(request,codigo):

    #eventos = Evento.objects.get(id=codigo)
    eventos = get_object_or_404(Evento,id=codigo)

    #"select * from Eventos where id=codigo"

    data = {
        'titulo': "Detalle Evento: " + str(codigo),
        'listado': eventos
    }

    return render(request,"detalle.html",data)

def about(request):
    data = {
        'titulo': "About...",
        'contenido': "esta es la pagina de about"
    }
    return render(request,"about.html",data)