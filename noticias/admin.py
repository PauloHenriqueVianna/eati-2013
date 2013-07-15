from django.contrib import admin #Import the admin
from noticias.models import Noticia #Import our todo Model
from tinymce.widgets import AdminTinyMCE
from django.db import models
   
class NoticiaAdmin(admin.ModelAdmin):        
    prepopulated_fields = {"url": ("titulo",)}
    readonly_fields = ('criado_por',)
    list_filter = ['criado_por','publicado']
    fields = ('titulo','url','criado_por','publicado','texto',)
    list_display = ('titulo','criado_em', 'criado_por', 'publicado')
    list_editable = ('publicado',)
    formfield_overrides = {
        models.TextField: {'widget': AdminTinyMCE},
    }        
        
    def save_model(self, request, obj, form, change): 
        obj.criado_por = request.user
        obj.save()

    def save_formset(self, request, form, formset, change): 
        if formset.model == Noticia:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.criado_por = request.user
                instance.save()
        else:
            formset.save()


admin.site.register(Noticia, NoticiaAdmin) 