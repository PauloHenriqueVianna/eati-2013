from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.db import transaction
from django.db.models import F
from models import Estados, Participantes, ParticipantesAtividades, AtividadesAdicionais, IdsDisponiveis, EventosInscricao

evento = 2

def Index(request):
	ctoken = {}
	ctoken.update(csrf(request))
	print getNumeroIncricao()
	return render_to_response('inicio.html', RequestContext(request, {}))

def VerificaInscricao(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		email = request.POST.get('email')
		request.session['email'] = email
		num = Participantes.objects.filter(email=email, id_categoria__id_evento=evento).count()
		if num > 0:
			return render_to_response('resultadoVerificacao.html', RequestContext(request, {'email':email}))
		else:
			email = request.session['email']
			atividades = AtividadesAdicionais.objects.filter(id_evento=evento)
			return render_to_response('formularioInscricao.html', RequestContext(request, {'email':email, 'atividades':atividades}))
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

@transaction.commit_manually
def getUltimoId(tabela):
	IdsDisponiveis.objects.filter(nome_tabela=tabela).update(ult_id=F('ult_id') + 1)
	ultId = IdsDisponiveis.objects.get(nome_tabela=tabela)
	transaction.commit()
	return ultId.ult_id

@transaction.commit_manually
def getNumeroIncricao():
	EventosInscricao.objects.filter(id_evento=evento).update(ult_nr_inscr=F('ult_nr_inscr') + 1)
	ultNrIsnc = EventosInscricao.objects.get(id_evento=evento)
	transaction.commit()
	return ultNrIsnc.ult_nr_inscr