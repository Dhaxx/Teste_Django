# urls.py no app do carrossel
from django.urls import path
from .views import servicos_view

urlpatterns = [
    path('', servicos_view, name='servicos'),
]