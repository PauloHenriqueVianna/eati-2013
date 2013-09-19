from django.conf.urls import patterns, url
from views import Index, VerificaInscricao, EnviaNumeroInscricao, ConsultaInscricao, CadastraInscricao

urlpatterns = patterns('inscricoes',
    url(r'^$', Index),
    url(r'^verifica/$', VerificaInscricao),
    url(r'^consulta/$', ConsultaInscricao),
    url(r'^envia/$', EnviaNumeroInscricao),
    url(r'^cadastra/$', CadastraInscricao),
)