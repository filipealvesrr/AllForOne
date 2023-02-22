from django.shortcuts import render
from dashboard.models import Caso, Category
from django.contrib import messages  # noqa: F401


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


def new_case(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/pages/new-case.html', context={
        'categories': categories,
    })


def my_cases(request):
    cards = Caso.objects.filter(
        is_published=False
    ).order_by('-id')
    return render(request, 'dashboard/pages/my-cases.html', context={
        'cards': cards,
        'is_empty': len(cards) == 0,
        'is_dash': True,
    })
