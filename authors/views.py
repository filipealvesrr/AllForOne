from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'authors/pages/register_view.html', context={
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST

    form = RegisterForm(POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        messages.success(
            request, 'Usuário cadastrado com sucesso!'
            'Faça seu Login')
        del (request.session['register_form_data'])
        return redirect('authors:login')

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', context={
        'form': form,
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticate_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticate_user is not None:
            login(request, authenticate_user)
        else:
            messages.error(request, 'As credenciais estão inválidas!')
    else:
        messages.error(request, 'Username ou senha inválidos!')

    return redirect('dashboard:home')


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    return redirect('authors:login')


def reset_done(request):
    return render(request, )
