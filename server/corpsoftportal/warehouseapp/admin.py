from django.contrib import admin
from warehouseapp.models import Warehouse, WarehouseType
# Register your models here.


admin.site.register(Warehouse)
admin.site.register(WarehouseType)