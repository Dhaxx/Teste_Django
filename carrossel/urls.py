# urls.py no app do carrossel
from django.urls import path
from .views import carrossel_view

urlpatterns = [
    path('carrossel/', carrossel_view, name='carrossel_view'),
]
