from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from softwareapp.models import Category
from softwareapp.forms import CategoryCreateForm, SofwareCreateForm

# Create your views here.


def main(request):
    return render(request, 'softwareapp/base.html', {})


def catalog_soft(request):
    query = Category.objects.all()
    return render(request, 'softwareapp/catalog_soft.html', {'results': query})

#
def category_create(request):
    title = 'Создание категории'
    # Вывод формы для редактирования
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CategoryCreateForm()

    content = {
        'title': title,
        'form': form
    }
    # creation_form = CategoryCreateForm(data=request.POST or None)
    #
    # if request.method == 'POST' and creation_form.is_valid():
    #     name = request.POST['name']
    #     license_type = request.POST['license_type']
    #
    # content = {'title': title, 'add_form': creation_form}

    return render(request, 'softwareapp/category_creation.html', content)


def create_form(request):
    return render(request, 'softwareapp/category_creation.html')
