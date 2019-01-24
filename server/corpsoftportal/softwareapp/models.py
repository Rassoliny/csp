from django.db import models

# Create your models here.


class Category(models.Model):
    """software category model class"""
    name = models.CharField(max_length=128)
    license_type = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Software(models.Model):
    """software class"""

    class Meta:
        verbose_name = "Софт"
        verbose_name_plural = "Софт"

    name = models.CharField("Название", max_length=128)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class LicenseType(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Типы лицензий"
