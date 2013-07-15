# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Palestrante(models.Model):
    
    palestrante     =   models.CharField(blank = False, max_length=240)
    trabalho        =   models.CharField(max_length=240, verbose_name = u"onde trabalha")
    sobre           =   models.TextField(blank = False, verbose_name = u"sobre/perfil")
    avatar          =   models.ImageField(verbose_name = u'foto', upload_to='palestrante/', blank = True)
    slug            =   models.SlugField(unique = True, blank=False)
    
    def get_absolute_url(self):
        return reverse('atividades.views.palestrante', kwargs={'slug': self.slug})
    
    def __unicode__(self):
        return self.palestrante
    

class Atividade(models.Model):
    evento = (
        ('data', 'data'),
        ('palestra', 'palestra'),
        ('minicurso', 'minicurso'),
        ('evento', 'evento'),
    )
    
    class Meta:
        ordering = ["data","inicio"]
        
    tema        =   models.CharField(max_length=240, blank=False)
    url         =   models.SlugField(unique = True, blank = False)
    tipo        =   models.CharField(verbose_name=u'tipo de atividade',max_length=100,choices=evento, blank=False)
    palestrante =   models.ForeignKey(Palestrante, blank = True, null=True)
    desc        =   models.TextField(blank = False)
    local       =   models.CharField(max_length=140)
    data        =   models.DateField(blank = False)
    inicio      =   models.TimeField(verbose_name= u"horário de início", blank = True)
    fim         =   models.TimeField(verbose_name= u"horário de encerramento", blank = True)
    
    
    def get_absolute_url(self):
        return reverse('atividades.views.atividade', kwargs={'slug': self.url})
    
    def __unicode__(self):
        return self.tema