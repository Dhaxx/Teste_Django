from django.urls import path
from .views import blog

urlpatterns = [
    path('', blog, name='blog'),
    path('blog/<str:categoria>/', blog, name='blog_categoria'),
]
