from django.urls import path
from contas import views

app_name = 'contas'

urlpatterns = [
    path('entrar/', views.login, name = 'entrar'),
    path('esqueci-a-senha/', views.esqueceu_senha, name = 'esqueci'),
    path('lembrar/', views.lembrar, name = 'lembrar'),
    path('inscrever/', views.inscrever, name = 'inscrever'),    
]
