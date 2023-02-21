from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('new-case/', views.new_case, name='newcase'),
    path('my-cases/', views.my_cases, name='mycases'),

]
