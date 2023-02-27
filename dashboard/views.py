from django.shortcuts import render, redirect
from django.http import Http404
from .forms import NewCaseForm
from dashboard.models import Caso, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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
    register_form_data = request.session.get('register_form_data', None)
    form = NewCaseForm(register_form_data)

    return render(request, 'dashboard/pages/new-case.html', context={
        'form': form,
    })


@login_required(login_url='authors:login', redirect_field_name='next')
def new_case_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = NewCaseForm(POST)
    if form.is_valid():
        category_name = form.cleaned_data['category']
        category, _ = Category.objects.get_or_create(name=category_name)
        caso: Caso = form.save(commit=False)
        caso.value_received = 0.0
        caso.usuario = request.user
        caso.category = category
        caso.is_published = False
        caso.save()

        del (request.session['register_form_data'])
        return redirect('dashboard:mycases')
    else:
        print(form.errors)

    return redirect('dashboard:newcase')


@login_required(login_url='authors:login', redirect_field_name='next')
def my_cases(request):
    usuario = request.user
    cards = Caso.objects.filter(
        is_published=False,
        usuario=usuario,
    ).order_by('-id')

    p = Paginator(cards,4)
    page = request.GET.get('page')
    card_list = p.get_page(page)

    return render(request, 'dashboard/pages/my-cases.html', context={
        'cards': cards,
        'is_empty': len(cards) == 0,
        'is_dash': True,
        'card_list': card_list
    })
