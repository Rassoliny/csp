from django.shortcuts import render
from warehouseapp.models import Warehouse
from warehouseapp.forms import WarehouseCreateForm

# Create your views here.


def main(request):
    return render(request, 'warehouseapp/base.html', {})


def warehouse_create(request):
    title = 'Создание склада'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = WarehouseCreateForm(request.POST)
        if form.is_valid():
            print(request.POST['name'])
            # category = Warehouse(name=request.POST['name'], license_type=LicenseType.objects.get(id=request.POST['license_type']))
            # category.save()
            return HttpResponseRedirect(reverse('warehouseapp:main'))
    else:
        form = WarehouseCreateForm()

    content = {
        'title': title,
        'form': form
    }

    return render(request, 'warehouseapp/warehouse_creation.html', content)
