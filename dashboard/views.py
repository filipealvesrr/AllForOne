from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def new_case(request):
    return render(request, 'dashboard/new-case.html')


def my_cases(request):
    return render(request, 'dashboard/my-cases.html')
