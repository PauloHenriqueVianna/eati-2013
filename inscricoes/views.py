from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.db import transaction
from django.db.models import F
from models import Estados, Participantes, ParticipantesAtividades, AtividadesAdicionais, IdsDisponiveis, EventosInscricao, Categorias

evento = 3

def Index(request):
	ctoken = {}
	ctoken.update(csrf(request))
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

def CadastraInscricao(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		b = Participantes()
		b.email = request.POST.get('email')
		b.nome = request.POST.get('nome')
		b.sexo = request.POST.get('sexo')
		b.instituicao = request.POST.get('instituicao')
		categoria = Categorias.objects.get(id_categoria=request.POST.get('categoria'))
		b.id_categoria = categoria
		b.endereco = request.POST.get('endereco')
		b.complemento = request.POST.get('complemento')
		b.cep = request.POST.get('cep')
		b.cidade = request.POST.get('municipio')
		estado = Estados.objects.get(uf=request.POST.get('uf'))
		b.uf = estado
		b.id_participante = getUltimoId('PARTICIPANTES')
		b.num_inscricao = getNumeroIncricao()
		b.save()
		atividades = request.POST.getlist('atividades[]')
		for a in atividades:
			atividade = AtividadesAdicionais.objects.get(id_atividade=a)
			atividade1 = ParticipantesAtividades(id_atividade=atividade,id_participante=b)
			atividade1.save()
		participante = Participantes.objects.get(email=b.email, id_categoria__id_evento=evento, num_inscricao=b.num_inscricao)
		atividades = ParticipantesAtividades.objects.filter(id_participante=b.id_participante, id_atividade__id_evento=evento)
		return render_to_response('dadosInscricao.html', RequestContext(request, {'participante':participante, 'atividades':atividades, 'nova':True}))
	else:
		return render_to_response('inicio.html', RequestContext(request, {}))


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
	return Ean13(str(ultNrIsnc.ult_nr_inscr))

def Ean13(ultNrIsnc):
	string = ultNrIsnc.rjust(12,'0')
	soma = 0
	for i in range (0,12):
		if i%2 == 0:
			soma = soma + (int(string[i]) * 1)
		else:
			soma = soma + (int(string[i]) * 3)
	multiplo = soma
	while multiplo%10 != 0:
		multiplo += 1
	dv = multiplo - soma
	return ultNrIsnc + str(dv)
