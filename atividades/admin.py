from django.contrib import admin #Import the admin
from models import Atividade, Palestrante
from tinymce.widgets import AdminTinyMCE
from django.db import models

class AtividadeAdmin(admin.ModelAdmin):        
    prepopulated_fields = {"url": ("tema",)}
    list_filter = ['data','inicio', 'local']
    list_display = ('tema','palestrante', 'data', 'inicio')

admin.site.register(Atividade, AtividadeAdmin)

class PalestranteAdmin(admin.ModelAdmin):        
    prepopulated_fields = {"slug": ("palestrante",)}
    list_filter = ['trabalho',]
    list_display = ('palestrante', 'trabalho')

admin.site.register(Palestrante, PalestranteAdmin)