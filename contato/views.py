from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.core.mail import send_mail,EmailMessage

def apoio(request):
	ctoken = {}
	ctoken.update(csrf(request))
	return render_to_response('apoio.html', RequestContext(request, {}))

def fale(request):
	ctoken = {}
	ctoken.update(csrf(request))
	return render_to_response('fale-conosco.html', RequestContext(request, {}))

def enviar(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		nome = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		flag = request.POST.get('flag')
		if flag == 'apoio':
			empresa = request.POST.get('company')
			empresa_assunto = empresa
			assunto = 'Apoio IV EATI'
			pagina = 'apoio.html'
			destino = 'eati.organizacao@cafw.ufsm.br'
			if empresa != '':
				mensagem = '<b>Nome:</b> ' + nome + ' <br> <b>Empresa:</b> ' + empresa + ' <br><br> ' + message
			else:
				mensagem = '<b>Nome:</b> ' + nome + ' <br><br> ' + message
		else:
			assunto = request.POST.get('subject')
			empresa_assunto = assunto
			pagina = 'fale-conosco.html'
			destino = 'eati@cafw.ufsm.br'
			mensagem = '<b>Nome:</b> ' + nome + ' <br><br> ' + message
		msg = EmailMessage(assunto, mensagem, email, [destino],headers = {'Reply-To': email})
		msg.content_subtype = "html"
		if msg.send():
			return render_to_response(pagina, RequestContext(request, {'enviado':1}))
		else:
			return render_to_response(pagina, RequestContext(request, {'enviado':2,'nome':nome,'empresa_assunto':empresa_assunto,'email':email,'mensagem':message}))