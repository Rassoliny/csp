from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from warehouseapp.models import Warehouse, WarehouseType
from warehouseapp.forms import WarehouseCreateForm
# Create your views here.


@login_required
def main(request):
    return render(request, 'warehouseapp/base.html', {})


@login_required
def warehouse_create(request):
    title = 'Создание склада'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = WarehouseCreateForm(request.POST)
        if form.is_valid():
            warehouse = Warehouse(name=request.POST['name'], warehouse_type=WarehouseType.objects.get(id=request.POST['warehouse_type']))
            warehouse.save()
            return HttpResponseRedirect(reverse('warehouseapp:main'))
    else:
        form = WarehouseCreateForm()

    content = {
        'title': title,
        'form': form
    }

    return render(request, 'warehouseapp/warehouse_creation.html', content)

