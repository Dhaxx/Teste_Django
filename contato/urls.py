# contato/urls.py

from django.urls import path
from .views import MinhaViewDoFormulario

urlpatterns = [
    path('contato/', MinhaViewDoFormulario.as_view(), name='contato'),
]
