from django import forms
from .models import Contacto,tipo_contacto

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
    
    tipo = forms.ChoiceField(choices=tipo_contacto,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }))

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Mensaje'
        }))
   
    class Meta:
        model= Contacto
        fields= ["nombre","correo","tipo","mensaje"]


        
    
