from django import forms
from .models import Contacto

class FormContacto(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Ingrese Nombre",
        }))
    
    correo = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"name@example.com",
        }))
   
    class Meta:
        model= Contacto
        fields= ["nombre","correo","tipo","mensaje"]


        
    
