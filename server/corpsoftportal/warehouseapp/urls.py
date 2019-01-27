from django.urls import path
from warehouseapp import views as warehouseapp

app_name = 'warehouseapp'

urlpatterns = [
    path('', warehouseapp.main, name='main'),
]
