from django.core.validators import MinValueValidator
from django.db import models
from datetime import datetime


class Car(models.Model):
    model = models.CharField(max_length=50, null=False, verbose_name='Modelo')
    brand = models.CharField(max_length=50, null=False, verbose_name='Marca')
    year = models.PositiveIntegerField(validators=[MinValueValidator(2000)], null=False, verbose_name='Ano')
    value = models.FloatField(null=False, verbose_name='Valor')
    register_date = models.DateTimeField(default=datetime.now(), null=False, verbose_name='Data de Cadastro')