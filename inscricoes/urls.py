from django.conf.urls import patterns, url
from views import Index, VerificaInscricao, ConsultaInscricao

urlpatterns = patterns('inscricoes',
    url(r'^$', Index),
    url(r'^verifica/$', VerificaInscricao),
    url(r'^consulta/$', ConsultaInscricao),
)