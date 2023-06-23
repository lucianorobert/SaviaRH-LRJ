"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from user import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('register/', views.register, name='user-register'),
    path('profile/<int:pk>/', views.profilePk, name='user-profile'),
    path('profile/', views.profile, name='user-profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("cambiar-password/", views.cambiar_password, name="cambiar-password"),
    path("reset-password/", views.password_reset_request, name="reset-password"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    # path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    
]
