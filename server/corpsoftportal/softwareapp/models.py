from django.db import models
from warehouseapp.models import Warehouse


# Create your models here.
class LicenseType(models.Model):
    """class license type"""
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Типы лицензий"
        verbose_name_plural = "Типы лицензий"

    def __str__(self):
        return self.name


class LicenseTerm(models.Model):
    name = models.CharField(max_length=32)
    """class license term"""
    class Meta:
        verbose_name = "Срок действия лицензии"
        verbose_name_plural = "Срок действия лицензии"

    def __str__(self):
        return self.name


class Category(models.Model):
    """software category model class"""
    name = models.CharField(max_length=128)
    license_type = models.ForeignKey(
        LicenseType, verbose_name='Тип лицензии', on_delete=models.CASCADE, blank=True)

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
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=True)
    license_term = models.ForeignKey(LicenseTerm, verbose_name='Срок лицензии', on_delete=models.CASCADE, blank=True)
    license_key = models.TextField("Лицензионный ключ", max_length=128, blank=True)
    # 3 - склад нераспределенного ПО
    owner = models.ForeignKey(Warehouse, verbose_name='Владелец', on_delete=models.CASCADE, default=3)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    """class transfer"""
    source = models.ForeignKey(Warehouse, related_name='sender', on_delete=models.CASCADE, verbose_name='Отправитель')
    destination = models.ForeignKey(Warehouse, related_name='reciever', on_delete=models.CASCADE, verbose_name='Получатель')
    software = models.ForeignKey(Software, verbose_name='Передаваемый софт', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Проводка"
        verbose_name_plural = "Проводки"
