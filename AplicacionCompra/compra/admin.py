from django.contrib import admin
from .models import producto
from .models import categoria


admin.site.register(producto)
admin.site.register(categoria)