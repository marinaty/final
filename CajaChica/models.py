from django.db import models
from django.utils import timezone

# Create your models here.
class Cuentas(models.Model):
    nombre = models.CharField('nombre cuenta',max_length=50, unique=True)
    descripcion = models.CharField('descripcion cuenta',max_length=50, unique=False)

class Transacciones(models.Model):
    trans_descrip = models.CharField('descripcion taransaccion', max_length=255)
    fecha = models.DateTimeField(default=timezone.now)
    tipo = models.BooleanField('in/egreso', default=True)
    monto = models.IntegerField()
    cuenta = models.ForeignKey(Cuentas)
