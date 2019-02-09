from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from softwareapp.models import Category, LicenseType, Software, LicenseTerm, Transfer
from softwareapp.forms import CategoryCreateForm, SofwareCreateForm, TransferCreateForm
from warehouseapp.models import Warehouse, WarehouseType
import json


# Create your views here.


def main(request):
    unclassifed = Software.objects.filter(owner=3)
    content = {
        'unclassifed': unclassifed,
    }
    return render(request, 'softwareapp/base.html', content)


def catalog_soft(request):
    categories = Software.objects.all()
    software = Software.objects.all()

    content = {
        'categories': categories,
        'software': software
    }

    return render(request, 'softwareapp/catalog_soft.html', content)


def category_create(request):
    title = 'Создание категории'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            category = Category(name=request.POST['name'],
                                license_type=LicenseType.objects.get(id=request.POST['license_type']))
            category.save()
            return HttpResponseRedirect(reverse('softwareapp:main'))
    else:
        form = CategoryCreateForm()

    content = {
        'title': title,
        'form': form
    }

    return render(request, 'softwareapp/category_creation.html', content)


def software_create(request):
    title = 'Создание категории'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = SofwareCreateForm(request.POST)
        if form.is_valid():
            software = Software(name=request.POST['name'],
                                category=Category.objects.get(id=request.POST['category']),
                                license_term=LicenseTerm.objects.get(id=request.POST['license_term']),
                                license_key=request.POST['license_key'])
            software.save()

            return HttpResponseRedirect(reverse('softwareapp:main'))
    else:
        form = SofwareCreateForm()

    content = {
        'title': title,
        'form': form
    }

    return render(request, 'softwareapp/software_creation.html', content)


def transfer_create(request):
    title = 'Проводка'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = TransferCreateForm(request.POST)
        if form.is_valid():
            software = Software.objects.get(id=request.POST['software'])
            software.owner = Warehouse.objects.get(id=request.POST['destination'])
            software.save()

            return HttpResponseRedirect(reverse('softwareapp:main'))
    else:
        form = TransferCreateForm()

    content = {
        'title': title,
        'form': form
    }

    return render(request, 'softwareapp/transfer_creation.html', content)


@csrf_exempt
def reciever(request):
    if request.method == "POST":
        data = json.loads(json.loads(request.body))
        try:
            host = Warehouse.objects.get(name=data['machine_name'])
        except:
            host = Warehouse(name=data['machine_name'], warehouse_type=WarehouseType.objects.get(id=2))
            host.save()
        print(data['username'])
        # print(data['soft'])
        for software in data['soft']:
            try:
                software_name = Software.objects.get(name=software['DisplayName'],
                                                     owner_id=Warehouse.objects.get(name=data['machine_name']))
            except:
                # print(Warehouse.objects.get(name=data['machine_name']))
                software_name = Software(name=software['DisplayName'],
                                         owner_id=Warehouse.objects.get(name=data['machine_name']).id,
                                         category_id=Category.objects.get(name='Unknown').id,
                                         license_term_id=LicenseTerm.objects.get(name='Unknown').id)
                software_name.save()

    return render(request, 'softwareapp/base.html', {})
