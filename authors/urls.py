from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_view, name='create'),

]
