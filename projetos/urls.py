# urls.py no app do carrossel
from django.urls import path
from .views import projetos, projeto_detalhado

urlpatterns = [
    path('', projetos, name='projetos'),
    path('<str:tipo_projeto>/', projetos, name='projetos_filtrados'),
    path('detalhes/<str:titulo>/', projeto_detalhado, name='detalhes_projeto'),
]