from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='Marca')
    category = models.CharField(max_length=50, null=False, verbose_name='Categoria')

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.CharField(max_length=50, null=False, verbose_name='Descrição')
    price = models.FloatField(null=False, verbose_name='Preço')
    brand = models.ForeignKey(Brand, verbose_name='Marca')