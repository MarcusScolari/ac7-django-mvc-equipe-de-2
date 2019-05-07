from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def esqueceu_senha(request):
    return render(request, 'esqueci.html')

def inscrever(request):
    return render(request, 'inscrever.html')

def lembrar(request):
    return render(request, 'lembrar.html')