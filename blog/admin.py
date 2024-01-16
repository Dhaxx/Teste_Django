from django.contrib import admin
from .models import Postagem, Categoria

# Register your models here.
admin.site.register(Postagem)
admin.site.register(Categoria)