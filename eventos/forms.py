from django import forms
from .models import Contacto,tipo_contacto

class FormContacto(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder":"Ingrese Nombre",
        }))
    
    
    correo = forms.EmailField(
        widget=forms.TextInput(attrs={
            "placeholder":"name@example.com",
        }))
    
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Mensaje'
        }))
   
    class Meta:
        model= Contacto
        fields= ["nombre","correo","tipo","mensaje"]


        
    
