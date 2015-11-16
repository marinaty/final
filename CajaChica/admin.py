from django.contrib import admin

# Register your models here.
from .models import Cuentas
from .models import Transacciones

admin.site.register(Cuentas)
admin.site.register(Transacciones)
