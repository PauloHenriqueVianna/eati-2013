from django.contrib import admin
from maratona.models import Equipes
from django.db import models
   
class EquipesAdmin(admin.ModelAdmin):
    list_display = ('equipe', 'dataInscricao', 'integrante01')      

admin.site.register(Equipes, EquipesAdmin) 