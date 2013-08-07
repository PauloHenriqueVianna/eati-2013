from django.conf.urls import patterns, include, url
from eati.feeds import TodasNoticias, UltimasNoticias
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'noticias.views.home', name='home'),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
     
    #funcionar todas as noticias
    (r'^noticias/$', 'noticias.views.noticias'),

    #funcionar slug das noticias
	(r'^noticia/(?P<slug>[\w_-]+)/$', 'noticias.views.noticia'),
     
    #funcionar slug das atividades
	(r'^atividade/(?P<slug>[\w_-]+)/$', 'atividades.views.atividade'),
     
    # Required to make static serving work 
	url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),

    #tinymce
    (r'^tinymce/', include('tinymce.urls')),

    #contato
    url(r'^contato/', include('contato.urls')),

    #feed
    (r'^feed/$', TodasNoticias()),
    (r'^feed/ultimas/$', UltimasNoticias()),
)