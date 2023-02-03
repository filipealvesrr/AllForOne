from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('new-case/', views.new_case),
]
