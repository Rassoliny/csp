from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from softwareapp.models import Category, LicenseType, Software, LicenseTerm
from softwareapp.forms import CategoryCreateForm, SofwareCreateForm

# Create your views here.


def main(request):
    return render(request, 'softwareapp/base.html', {})


def catalog_soft(request):
    query = Software.objects.all()
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


def software_create(request):
    title = 'Создание категории'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = SofwareCreateForm(request.POST)
        if form.is_valid():
            software = Software(name=request.POST['name'],
                                category=Category.objects.get(id=request.POST['category']),
                                license_term=LicenseTerm.objects.get(id=request.POST['license_term']))
            software.save()

            return HttpResponseRedirect(reverse('softwareapp:main'))
    else:
        form = SofwareCreateForm()

    content = {
        'title': title,
        'form': form
    }

    return render(request, 'softwareapp/software_creation.html', content)
