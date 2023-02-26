from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewCaseForm
from dashboard.models import Caso
from django.contrib.auth.decorators import login_required


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    cards = Caso.objects.filter(
        is_published=True
    ).order_by('-id')

    return render(request, 'dashboard/pages/dashboard.html', context={
        'cards': cards,
        'is_empty': len(cards) == 0,
        'is_dash': True,
        'is_card_dash': True,
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def new_case(request):
    form = NewCaseForm(request.POST)
    # if request.method == "POST":
    #     title_case = request.POST.get('title-case', None)
    #     category = request.POST.get('category', None)
    #     description = request.POST.get('description', None)
    #     value_total = request.POST.get('value_total', None)
    #     date_end = request.POST.get('date-end', None)

    return render(request, 'dashboard/pages/new-case.html', context={
        'form': form,
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def my_cases(request):
    usuario = request.user
    cards = Caso.objects.filter(
        is_published=False,
        usuario=usuario,
    ).order_by('-id')
    return render(request, 'dashboard/pages/my-cases.html', context={
        'cards': cards,
        'is_empty': len(cards) == 0,
        'is_dash': True,
    })
