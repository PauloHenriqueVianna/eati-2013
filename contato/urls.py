from django.conf.urls import patterns, url
from views import apoio, fale, enviar

urlpatterns = patterns('contato',
    #url(r'^$', Inicio),
    url(r'^apoio/$',apoio),
    url(r'^fale-conosco/$',fale),
    url(r'^enviar/$',enviar),
)