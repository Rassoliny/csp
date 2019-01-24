from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from softwareapp.models import Category, LicenseType
from softwareapp.forms import CategoryCreateForm, SofwareCreateForm

# Create your views here.


def main(request):
    return render(request, 'softwareapp/base.html', {})


def catalog_soft(request):
    query = Category.objects.all()
    return render(request, 'softwareapp/catalog_soft.html', {'results': query})


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


def create_form(request):
    return render(request, 'softwareapp/category_creation.html')
