from django.conf.urls import patterns, url
from views import apoio, enviar

urlpatterns = patterns('contato',
    #url(r'^$', Inicio),
    url(r'^apoio/$',apoio),
    url(r'^enviar/$',enviar),
)