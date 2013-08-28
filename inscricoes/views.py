from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from models import Estados, Participantes, ParticipantesAtividades

evento = 2

def Index(request):
	ctoken = {}
	ctoken.update(csrf(request))
	return render_to_response('inicio.html', RequestContext(request, {}))

def VerificaInscricao(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		email = request.POST.get('email')
		num = Participantes.objects.filter(email=email, id_categoria__id_evento=evento).count()
		if num > 0:
			request.session['email'] = email
			return render_to_response('resultadoVerificacao.html', RequestContext(request, {'email':email}))
		else:
			return render_to_response('inicio.html', RequestContext(request, {}))
	return render_to_response('inicio.html', RequestContext(request, {}))

def ConsultaInscricao(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		email = request.POST.get('email')
		inscricao = request.POST.get('inscricao')
		try:
			participante = Participantes.objects.get(email=email, id_categoria__id_evento=evento, num_inscricao=inscricao)
			atividades = ParticipantesAtividades.objects.filter(id_participante=participante.id_participante, id_atividade__id_evento=evento)
			return render_to_response('dadosInscricao.html', RequestContext(request, {'participante':participante, 'atividades':atividades}))
		except:
			return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email,'erro':True}))
	else:
		email = request.session['email']
		return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email}))