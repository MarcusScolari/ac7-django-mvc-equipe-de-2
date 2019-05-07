from django.urls import path

from restrito import views

app_name = 'restrito'

urlpatterns = [
    path('notas/', views.notas, name='notas')
]