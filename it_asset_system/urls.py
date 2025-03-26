# filepath: /home/kevincole/Development/kcse2024/it_asset_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from it_asset import views as it_asset_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', it_asset_views.user_profile, name='user_profile'),
    path('register/', it_asset_views.register, name='register'),
    path('', it_asset_views.asset_list, name='home'),  # Update this line to point to asset_list view
    path('about/', it_asset_views.about, name='about'),
    # path('contact/', it_asset_views.contact, name='contact'),
    path('asset-dashboard/', it_asset_views.asset_dashboard_view, name='asset_dashboard'),
    path('profile/', it_asset_views.user_profile, name='user_profile'),
    path('profile/edit/', it_asset_views.profile_edit, name='profile_edit'),
    path('change-password/', it_asset_views.change_password, name='change_password'),
    path('assets/', include('it_asset.urls')),  # Include URLs from it_asset app
    path('logout/', it_asset_views.logout_view, name='logout'),  # Add this line
    path('admin/', admin.site.urls),
    path('assets/', include('it_asset.urls')),
]
