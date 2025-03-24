"""
URL configuration for it_asset_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from it_asset import views as it_asset_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', it_asset_views.user_profile, name='user_profile'),
    path('register/', it_asset_views.register, name='register'),
    path('', it_asset_views.asset_list, name='home'),  # Update this line to point to asset_list view
    path('about/', it_asset_views.about, name='about'),
    path('contact/', it_asset_views.contact, name='contact'),
    path('asset-dashboard/', it_asset_views.asset_dashboard_view, name='asset_dashboard'),
    path('profile/', it_asset_views.user_profile, name='user_profile'),
    path('profile/edit/', it_asset_views.profile_edit, name='profile_edit'),
    path('change-password/', it_asset_views.change_password, name='change_password'),
    path('assets/', it_asset_views.asset_list, name='asset_list'),
    path('assets/add/', it_asset_views.add_asset, name='add_asset'),
    path('assets/<int:pk>/', it_asset_views.asset_detail, name='asset_detail'),
    path('assets/<int:pk>/update/', it_asset_views.asset_update, name='asset_update'),
    path('assets/<int:pk>/delete/', it_asset_views.asset_delete, name='asset_delete'),
]
