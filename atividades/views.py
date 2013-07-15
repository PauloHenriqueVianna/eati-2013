from django.shortcuts import render_to_response, get_object_or_404
from models import Atividade

def atividade(request, slug):
    actvs = get_object_or_404(Atividade, url=slug)
    return render_to_response('atividade.html', {'atv':actvs,})