from django.urls import path
from .views import blog, post_detalhado

urlpatterns = [
    path('', blog, name='blog'),
    path('blog/<str:categoria>/', blog, name='blog_categoria'),
    path('postagens/<str:titulo>/', post_detalhado, name='post_detalhado'),
]
