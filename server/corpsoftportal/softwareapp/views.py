from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from softwareapp.models import Category, LicenseType, Software, LicenseTerm, Transfer
from softwareapp.forms import CategoryCreateForm, SofwareForm, TransferCreateForm, SearchWarehouseForm
from warehouseapp.models import Warehouse, WarehouseType
import json


# Create your views here.


def main(request):
    """Основная страница
    Выводится список проблем, на которые стоит обратить внимание"""
    unknown_owner = Software.objects.filter(owner=Warehouse.objects.get(name='Нераспределенное ПО').id)
    unknown_category = Software.objects.filter(category=Category.objects.get(name='Unknown').id)

    content = {
        'unknown_owner': unknown_owner,
        'unknown_category': unknown_category
    }
    return render(request, 'softwareapp/base.html', content)


def catalog_soft(request):
    """Страница каталога"""
    categories = Category.objects.all()

    content = {
        'categories': categories
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
        form = SofwareForm(request.POST)
        if form.is_valid():
            software = Software(name=request.POST['name'],
                                category=Category.objects.get(id=request.POST['category']),
                                license_term=LicenseTerm.objects.get(id=request.POST['license_term']),
                                license_key=request.POST['license_key'])
            software.save()

            return HttpResponseRedirect(reverse('softwareapp:main'))
    else:
        form = SofwareForm()

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
    """Обработчик данных с хостов
    После приема данных требуется вручную расставить категории.
    После создания каталога софта эта проблема уйдет"""
    if request.method == "POST":
        data = json.loads(json.loads(request.body))
        if not Warehouse.objects.get(name=data['machine_name']).exists():
            host = Warehouse(name=data['machine_name'], warehouse_type=WarehouseType.objects.get(id=2))
            host.save()

        for software in data['soft']:
            if not Software.objects.get(name=software['DisplayName'],
                                        owner_id=Warehouse.objects.get(name=data['machine_name'])).exists():
                if software['DisplayName'] == '':
                    continue
                software_name = Software(name=software['DisplayName'],
                                         owner_id=Warehouse.objects.get(name=data['machine_name']).id,
                                         category_id=Category.objects.get(name='Unknown').id,
                                         license_term_id=LicenseTerm.objects.get(name='Unknown').id)
                software_name.save()

    return render(request, 'softwareapp/base.html', {})


def software_details(request, software_id):
    """Изменение записи софта"""
    instance = Software.objects.get(id=software_id)

    #Вывод формы для редактирования
    if request.method == "POST":
        form = SofwareForm(request.POST, instance=instance)
        if form.is_valid():
            instance.category_id = Category.objects.get(id=request.POST['category'])
            instance.license_term = LicenseTerm.objects.get(id=request.POST['license_term'])
            instance.owner = Warehouse.objects.get(id=request.POST['owner'])
            instance.license_key = request.POST['license_key']
            instance.save()
            return HttpResponseRedirect(reverse('softwareapp:main'))

    else:
        form = SofwareForm(instance=instance)

    content = {
        'itm': instance,
        'form': form
    }
    return render(request, 'softwareapp/detail.html', content)


def category_details(request, category_name):
    """Каталог софта внутри категории"""
    soft = Software.objects.filter(category=Category.objects.get(name=category_name))
    content = {
        'soft': soft,
        'category': category_name
    }
    return render(request, 'softwareapp/category_detail.html', content)


def check_warehouse(request):
    """Форма поиска склада"""
    form = SearchWarehouseForm()
    return render(request, 'softwareapp/check_warehouse.html', {'form': form})


def get_warehouse(request):
    """Список софта на указанном складе"""
    warehouse = request.POST['warehouse']
    try:
        soft = Software.objects.filter(owner=Warehouse.objects.get(name=warehouse))
        content = {
            'soft': soft,
            'category': warehouse
        }
        return render(request, 'softwareapp/category_detail.html', content)
    except:
        return HttpResponseRedirect(reverse('softwareapp:check_warehouse'))

