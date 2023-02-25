from django.shortcuts import render
from dashboard.models import Caso, Category
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
    categories = Category.objects.all()
    return render(request, 'dashboard/pages/new-case.html', context={
        'categories': categories,
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
