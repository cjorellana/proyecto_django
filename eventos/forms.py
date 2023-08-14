from django import forms
from .models import Contacto

class FormContacto(forms.ModelForm):
    class Meta:
        model= Contacto
        fields= ["nombre","correo","tipo","mensaje"]
        
    
