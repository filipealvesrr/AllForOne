from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
    path('logout/', views.logout_view, name='logout_view'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('rest-auth/password/reset/confirm/<str:uidb64>/<str:token>', auth_views.PasswordResetConfirmView.as_view(),  # noqa E501
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),  # noqa E501
         name="password_reset_complete"),

]
