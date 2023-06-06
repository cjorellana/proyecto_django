1.) install bootstrap
	1.1) pip instal bootstrap-v5
	1.2) Agregar a settitSg.py:

 INSTALLED_APPS = [    
    'bootstrap5',
]		

BASE.HTML
{% load bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}


2.) archivos staticos, js, css, img

1.) static
2.) js, css, img
3.) agregamos logo.png -> img

4.) agregar a settitSg.py:
STATIC_URL = 'static/'

5.) en base agregar:
{% load static %}

<img src = "{% static 'img/logo2.png' %}" alt="logo UG" width="60%" />