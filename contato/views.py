from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
from django.core.mail import send_mail,EmailMessage

def apoio(request):
	ctoken = {}
	ctoken.update(csrf(request))
	return render_to_response('apoio.html', RequestContext(request, {}))

def enviar(request):
	ctoken = {}
	ctoken.update(csrf(request))
	if request.method == 'POST':
		nome = request.POST.get('name')
		empresa = request.POST.get('company')
		email = request.POST.get('email')
		message = request.POST.get('message')
		if empresa != '':
			mensagem = '<b>Nome:</b> ' + nome + ' <br> <b>Empresa:</b> ' + empresa + ' <br><br> ' + message
		else:
			mensagem = '<b>Nome:</b> ' + nome + ' <br><br> ' + message
		msg = EmailMessage('Apoio IV EATI', mensagem, email, ['eati.organizacao@cafw.ufsm.br'],headers = {'Reply-To': email})
		msg.content_subtype = "html"
		if msg.send():
			return render_to_response('apoio.html', RequestContext(request, {'enviado':1}))
		else:
			return render_to_response('apoio.html', RequestContext(request, {'enviado':2,'nome':nome,'empresa':empresa,'email':email,'mensagem':message}))


