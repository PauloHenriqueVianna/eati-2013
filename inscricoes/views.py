# -*- coding: utf-8 -*-
import hashlib
from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.db import transaction
from django.db.models import F, Sum
from django.core.mail import send_mail,EmailMessage
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
			valorCategoria = participante.id_categoria.vl_categoria
			valorAtividades = atividades.aggregate(somaAtividades=Sum('id_atividade__vl_atividade'))
			atividades.soma = valorCategoria + valorAtividades['somaAtividades']
			atividades.soma = str(atividades.soma)
			atividades.soma.replace(',','.')
			participante.cod = hashlib.sha1("EA" + str(participante.id_participante) + "TI" + str(participante.num_inscricao)).hexdigest()
			return render_to_response('dadosInscricao.html', RequestContext(request, {'participante':participante, 'atividades':atividades}))
		except:
			erro = "A inscrição informada está incorreta."
			return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email,'erro':erro}))
	else:
		email = request.session['email']
		return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email}))

def EnviaNumeroInscricao(request):
	email = request.session['email']
	try:
		participante = Participantes.objects.get(email=email, id_categoria__id_evento=evento)
		try:
			mensagem = "<h3>Seu número de inscrição no " + participante.id_categoria.id_evento.nome_evento.encode("UTF-8") + " é:</h3>"
			mensagem += "<h1 style='color:red; text-align:center;'>" + str(participante.num_inscricao) + "</h1>"
			msg = EmailMessage('Número de Inscrição no IV EATI', mensagem, 'eati@cafw.ufsm.br', [email],headers = {'Reply-To': 'eati@cafw.ufsm.br'})
			msg.content_subtype = "html"
			msg.send()
			sucesso = "Seu número de inscrição foi enviado para o email " + email.encode("UTF-8") + "."
			return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email,'sucesso':sucesso}))
		except:
			erro = "Ocorreu um erro ao tentar enviar o e-mail, tente novamente."
			return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email,'erro':erro}))
	except:
		erro = "Não há inscrições realizadas com este e-mail."
		return render_to_response('consultaInscricao.html', RequestContext(request, {'email':email,'erro':erro}))

def CadastraInscricao(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		b = Participantes()
		b.email = request.POST.get('email')[0:198]
		b.nome = request.POST.get('nome')[0:98]
		b.sexo = request.POST.get('sexo')
		b.instituicao = request.POST.get('instituicao')[0:98]
		categoria = Categorias.objects.get(id_categoria=request.POST.get('categoria'))
		b.id_categoria = categoria
		b.endereco = request.POST.get('endereco')[0:98]
		b.complemento = request.POST.get('complemento')[0:98]
		b.cep = request.POST.get('cep')[0:9]
		b.cidade = request.POST.get('municipio')[0:98]
		estado = Estados.objects.get(uf=request.POST.get('uf'))
		b.uf = estado
		b.id_participante = getUltimoId('PARTICIPANTES')
		b.num_inscricao = getNumeroIncricao()
		try:
			b.save()
		except:
			return render_to_response('inicio.html', RequestContext(request, {}))
		atividadesForm = request.POST.getlist('atividades[]')
		if atividadesForm:
			for a in atividadesForm:
				atividade = AtividadesAdicionais.objects.get(id_atividade=a)
				atividade1 = ParticipantesAtividades(id_atividade=atividade,id_participante=b)
				atividade1.save()
			participante = Participantes.objects.get(email=b.email, id_categoria__id_evento=evento, num_inscricao=b.num_inscricao)
			atividades = ParticipantesAtividades.objects.filter(id_participante=b.id_participante, id_atividade__id_evento=evento)
			valorCategoria = participante.id_categoria.vl_categoria
			valorAtividades = atividades.aggregate(somaAtividades=Sum('id_atividade__vl_atividade'))
			atividades.soma = valorCategoria + valorAtividades['somaAtividades']
			atividadesTotal = str(atividades.soma)
		else:
			atividades = []
			participante = Participantes.objects.get(email=b.email, id_categoria__id_evento=evento, num_inscricao=b.num_inscricao)
			valorCategoria = participante.id_categoria.vl_categoria
			atividadesTotal = str(valorCategoria)
		atividadesTotal.replace(',','.')
		participante.cod = hashlib.sha1("EA" + str(participante.id_participante) + "TI" + str(participante.num_inscricao)).hexdigest()
		try:
			EnviarEmail(participante,atividades)
			return render_to_response('dadosInscricao.html', RequestContext(request, {'participante':participante, 'atividades':atividades, 'atividadesTotal':atividadesTotal, 'nova':True}))
		except:
			return render_to_response('dadosInscricao.html', RequestContext(request, {'participante':participante, 'atividades':atividades, 'atividadesTotal':atividadesTotal, 'nova':True}))
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

def EnviarEmail(participante,atividades):
	email = 'eati@cafw.ufsm.br'
	mensagem = "<h3>Sua inscrição no " + participante.id_categoria.id_evento.nome_evento.encode("UTF-8") + " foi realizada com sucesso, seguem os dados cadastrados:</h3>"
	mensagem += "<b>Nome:</b> " + participante.nome.encode("UTF-8") + "<br>"
	mensagem += "<b>Número de Incrição:</b> " + str(participante.num_inscricao) + "<br>"
	mensagem += "<b>E-mail:</b> " + participante.email.encode("UTF-8") + "<br>"
	mensagem += "<b>Sexo:</b> " + participante.getSexo().encode("UTF-8") + "<br>"
	mensagem += "<b>Instituição:</b> " + participante.instituicao.encode("UTF-8") + "<br>"
	mensagem += "<b>Categoria de Participação:</b> " + participante.id_categoria.descr_categoria.encode("UTF-8") + "<br>"
	mensagem += "<b>Endereço:</b> " + participante.endereco.encode("UTF-8") + "<br>"
	mensagem += "<b>Complemento:</b> " + participante.complemento.encode("UTF-8") + "<br>"
	mensagem += "<b>CEP:</b> " + participante.cep.encode("UTF-8") + "<br>"
	mensagem += "<b>Município:</b> " + participante.cidade.encode("UTF-8") + " - " + participante.uf.uf.encode("UTF-8")  + "<br>"
	mensagem += "<h4>Atividades Adicionais</h4>"
	for atividade in atividades:
		mensagem += "<p>" + atividade.id_atividade.descr_atividade.encode("UTF-8") + "</p>"
	msg = EmailMessage('Inscrição no IV EATI', mensagem, email, [participante.email],headers = {'Reply-To': email})
	msg.content_subtype = "html"
	if msg.send():
		return True
	else:
		return False