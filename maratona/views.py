# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from models import Equipes

def Regras(request):
	ctoken = {}
	ctoken.update(csrf(request))
	return render_to_response('regras.html', RequestContext(request, {}))

def Inscricao(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		try:
			if request.POST.get('equipe') != "" and request.POST.get('integrante01') != "" and request.POST.get('integrante02') != "" and request.POST.get('integrante03') != "" and request.POST.get('email01') != "":
				e = Equipes()
				e.equipe = request.POST.get('equipe')
				e.integrante01 = request.POST.get('integrante01')
				e.emailintegrante01 = request.POST.get('email01')
				e.integrante02 = request.POST.get('integrante02')
				e.emailintegrante02 = request.POST.get('email02')
				e.integrante03 = request.POST.get('integrante03')
				e.emailintegrante03 = request.POST.get('email03')
				e.integrante04 = request.POST.get('integrante04')
				e.emailintegrante04 = request.POST.get('email04')
				e.save()
				sucesso = "Sua inscrição foi realizada com sucesso."
				return render_to_response('regras.html', RequestContext(request, {'sucesso':sucesso}))
			else:
				erro = "Ocorreu um erro ao enviar os dados, preencha corretamente os campos e tente novamente."
				return render_to_response('regras.html', RequestContext(request, {'erro':erro}))
		except:
			erro = "Ocorreu um erro ao enviar os dados, preencha corretamente os campos e tente novamente."
			return render_to_response('regras.html', RequestContext(request, {'erro':erro}))
	return render_to_response('regras.html', RequestContext(request, {}))
