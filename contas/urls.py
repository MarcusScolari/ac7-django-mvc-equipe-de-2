from django.urls import path

from contas import views

app_name = 'contas'

urlpatterns = [
    path('esqueci-a-senha/', views.esqueci, name='esqueci'),
    path('lembrar/', views.lembrar, name='lembrar'),
    path('inscrever/', views.inscrever, name='inscrever'),
    path('entrar/', views.entrar, name='entrar')
]