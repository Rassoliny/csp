from django.urls import path
from softwareapp import views as sofwareapp

app_name = 'softwareapp'

urlpatterns = [
    path('catalog_soft', sofwareapp.catalog_soft, name='catalog_soft'),
    path('category_creation', sofwareapp.category_create, name='category_creation'),
    path('software_creation', sofwareapp.software_create, name='software_creation'),
    path('transfer_creation', sofwareapp.transfer_create, name='transfer_creation'),
    path('reciever', sofwareapp.reciever, name='reciever'),
    path('software_details/<int:software_id>', sofwareapp.software_details, name='software_details'),
    path('category_details/<str:category_name>', sofwareapp.category_details, name='category_details'),
    path('', sofwareapp.main, name='main'),
]
