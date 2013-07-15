from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from noticias.models import Noticia
 
def home(request):
    entries = Noticia.objects.filter(publicado=True)[:12]
    return render_to_response('news.html', {'posts' : entries})

def noticia(request, slug):
    c = {}
    c.update(csrf(request))
    new = get_object_or_404(Noticia, url=slug)        
    return render_to_response('new.html', {'new':new, 'c':c})