from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('client/', views.client_page, name='client_page'),
    path('staff/', views.staff_page, name='staff_page'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('profile-redirect/', views.profile_redirect, name='profile_redirect'),
]