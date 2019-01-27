from django.db import models

# Create your models here.


class Warehouse(models.Model):
    """class license type"""
    name = models.CharField(max_length=128)
    warehouse_type = models.CharField(max_length=32, default='Склад')

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"

    def __str__(self):
        return self.name
