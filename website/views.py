from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contato(request):
    if request.POST:
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        telefone = request.POST.get('telefone', '')
        assunto  = request.POST.get('assunto', '')
        mensagem = request.POST.get('mensagem', '')
        resposta = request.POST.getlist('resposta', '')

        if assunto == 'B': assunto = 'Bug'
        elif assunto == 'R': assunto = 'Reclamação'
        else: assunto = 'Sugestão'

        if len(email) > 0:
            # Montando o corpo da mensagem
            texto = "Você recebeu o contato do seguinte usuário:\n" \
            "->Nome: {nome}\n" \
            "->E-mail: {email}\n" \
            "->Telefone: {telefone}\n" \
            "->Assunto: {assunto}\n" \
            "->Resposta: {resposta}\n" \
            "->Mensagem: {mensagem}".format(
                nome=nome,
                email=email,
                telefone=telefone,
                assunto=assunto,
                resposta=';'.join(resposta).replace('T', 'Telefone').replace('E', 'E-mail') + ';',
                mensagem=mensagem)

            send_mail('FIT Contato - ' + assunto, texto, email, ['contato@fit.com.br'], fail_silently=False)

    return render(request, 'contato.html')