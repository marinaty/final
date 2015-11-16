# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(verbose_name='nombre cuenta', max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion cuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('trans_descrip', models.CharField(max_length=255, verbose_name='descripcion taransaccion')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('tipo', models.BooleanField(default=True, verbose_name='in/egreso')),
                ('monto', models.IntegerField()),
                ('cuenta', models.ForeignKey(to='CajaChica.Cuentas')),
            ],
        ),
    ]
