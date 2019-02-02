from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from softwareapp.models import Category, LicenseType, Software, LicenseTerm, Transfer
from softwareapp.forms import CategoryCreateForm, SofwareCreateForm, TransferCreateForm
from warehouseapp.models import Warehouse

# Create your views here.


def main(request):
    return render(request, 'softwareapp/base.html', {})


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
            category = Category(name=request.POST['name'], license_type=LicenseType.objects.get(id=request.POST['license_type']))
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
