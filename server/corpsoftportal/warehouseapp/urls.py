from django.urls import path
from warehouseapp import views as warehouseapp

app_name = 'warehouseapp'

urlpatterns = [
    path('warehouse_creation', warehouseapp.warehouse_create, name='warehouse_create'),
    path('', warehouseapp.main, name='main'),
]
