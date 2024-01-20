# contato/urls.py

from django.urls import path
from .views import contato_form

urlpatterns = [
    path('', contato_form, name='contato'),
]
