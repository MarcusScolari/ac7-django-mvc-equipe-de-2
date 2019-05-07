from django.urls import path
from restrito import views

app_name = 'restrito'

urlpatterns = [
    path('cursos/', views.ads, name = 'ads'),
    path('cursos/', views.bd, name = 'bd'),
    path('cursos/', views.gti, name = 'gti'),
    path('cursos/', views.si, name = 'si'),
]
