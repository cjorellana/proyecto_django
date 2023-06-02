from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'titulo': "Principal"
    }

    return render(request,"index.html",data)

def about(request):
    data = {
        'titulo': "About...",
        'contenido': "esta es la pagina de about"
    }
    return render(request,"about.html",data)