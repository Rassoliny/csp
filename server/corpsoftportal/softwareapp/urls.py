from django.urls import path
from softwareapp import views as sofwareapp

app_name = 'softwareapp'

urlpatterns = [
    path('catalog_soft', sofwareapp.catalog_soft, name='catalog_soft'),
    path('category_creation', sofwareapp.catalog_soft, name='category_creation'),
    path('', sofwareapp.main, name='main'),
]
