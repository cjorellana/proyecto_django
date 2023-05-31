from django.contrib import admin
from .models import Evento,Pais

# mejoras django-admin-interface
class EventoAdmin(admin.ModelAdmin):
    list_display= ["nombre","precio","inicio","fin",
                   "diploma","foto","activo","created_at"
                   ]
    search_fields = ["nombre"]
    list_filter = ["activo","diploma","inicio"]
    exclude = ["created_at"]

# Register your models here.
admin.site.register(Evento,EventoAdmin)
admin.site.register(Pais)