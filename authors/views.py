from django.shortcuts import render
from django.http import Http404
from .forms import RegisterForm
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'authors/pages/register_view.html', context={
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    form = RegisterForm(request.POST)
    return render(request, 'authors/pages/register_view.html', context={
        'form': form,
    })


def login(request):
    return render(request, 'authors/pages/login.html')
