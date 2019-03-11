from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib import auth
from ldap3 import Server, Connection, NTLM
from django.contrib.auth.models import User


# Create your views here.
def main(request):
    return render(request, 'authapp/base.html', {})


def login(request):
    login_form = LoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('softwareapp:main'))

    content = {
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('softwareapp:main'))
