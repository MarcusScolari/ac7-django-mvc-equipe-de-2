from django.urls import path
from cursos import views

app_name = 'cursos'

urlpatterns = [
    path('cursos/', views.ads, name = 'ads'),
    path('cursos/', views.bd, name = 'bd'),
    path('cursos/', views.gti, name = 'gti'),
    path('cursos/', views.si, name = 'si'),
]
