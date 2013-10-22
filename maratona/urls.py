from django.conf.urls import patterns, url
from views import Regras, Inscricao

urlpatterns = patterns('maratona',
    url(r'^$', Regras),
    url(r'^inscricao/$', Inscricao),
)