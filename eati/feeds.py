# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from noticias.models import Noticia

class UltimasNoticias(Feed):
    title = "Últimas Notícias IV EATI"
    link = "/"
    description = "Últimas Notícias do IV Encontro Anual de Tecnologia da Informação"

    def items(self):
        return Noticia.objects.order_by('-criado_em')[:6]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.texto

class TodasNoticias(Feed):
    title = "Notícias IV EATI"
    link = "/"
    description = "Notícias do IV Encontro Anual de Tecnologia da Informação"

    def items(self):
        return Noticia.objects.order_by('-criado_em')

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.texto
