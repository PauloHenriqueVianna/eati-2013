# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Noticia(models.Model):
    class Meta:
        ordering = ["-criado_em"]
    
    titulo      =   models.CharField(max_length=140, blank=False)
    url         =   models.SlugField(unique = True, blank=False)
    texto       =   models.TextField(blank = False)
    criado_por  =   models.ForeignKey(User, related_name='criado_por')
    criado_em   =   models.DateTimeField(auto_now_add = True)
    publicado   =   models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse('noticias.views.noticia', kwargs={'slug': self.url})
    
    def __unicode__(self):
        return 'Noticia: ' + self.titulo
    