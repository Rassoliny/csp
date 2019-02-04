from django.db import models
from django.apps import apps
# from softwareapp.models import Software
# # Create your models here.
# Software = apps.get_model('sofwareapp', 'Software')

class WarehouseType(models.Model):
    """class license type"""
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Тип склада"
        verbose_name_plural = "Типы складов"

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    """class license type"""
    name = models.CharField(verbose_name='Название склада', max_length=128)
    warehouse_type = models.ForeignKey(
        WarehouseType, verbose_name='Тип склада', on_delete=models.CASCADE, blank=True)
    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"

    def __str__(self):
        return self.name

