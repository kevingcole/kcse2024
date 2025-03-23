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
from it_asset import views
from django.urls import path, include
  
urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    # path('asset/<int:pk>/', views.asset_detail, name='asset_detail'),
    path('assets/<int:id>/', views.asset_detail, name='asset_detail'),
    #path('asset/new/', views.asset_create, name='asset_create'),
    #path('asset/<int:pk>/edit/', views.asset_update, name='asset_update'),
    #path('asset/<int:pk>/delete/', views.asset_delete, name='asset_delete'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the authentication URLs
    path('register/', views.register, name='register'),  # Registration URL
    path('', include('it_asset.urls')),  # Include your app's URLs
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('profile/', views.Profile, name='profile'),
    path('', include('it_asset.urls')),
]
