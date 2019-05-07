from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('contato/', views.contato, name = 'contato'),
    path('', views.index, name = 'index'),
]
