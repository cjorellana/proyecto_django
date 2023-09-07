from django.shortcuts import render,get_object_or_404
from .models import Evento
from .forms import FormContacto
from django.contrib import messages


# Create your views here.

def index(request):

    eventos = Evento.objects.all() # N

    data = {
        'titulo': "Principal",
        'listado': eventos
    }

    return render(request,"index.html",data)

def detalle(request,codigo):

    #eventos = Evento.objects.get(id=codigo) # 1
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

def contacto(request):

    data = {
        'form': FormContacto()
    }

    #metodo
    if request.method == 'POST':
        formulario= FormContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Soporte Enviado Correctamente. ')
        else:
            messages.error(request,'Error al enviar el formulario. ')
            data['form']=formulario
        
    return render(request,"contacto.html",data)
