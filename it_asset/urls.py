from django.urls import path, include
from . import views
from .views import user_profile_view
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from it_asset import views as it_asset_views

urlpatterns = [
    # Homepage and Static Pages
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Asset Management Dashboard
    path('asset-dashboard/', views.asset_dashboard_view, name='asset_dashboard'),

    # User Profile and Account Management
    path('profile/', user_profile_view, name='user_profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path("change-password/", views.change_password, name="change_password"),

    # Asset Management
    path("assets/<int:pk>/", it_asset_views.asset_detail, name="asset_detail"),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/add/', views.add_asset, name='add_asset'),
    path("assets/<int:pk>/update/", views.asset_update, name="asset_update"),
    path("assets/<int:pk>/delete/", views.asset_delete, name="asset_delete"),
    path('asset/<int:asset_id>/', views.asset_detail, name='asset_detail'),

    # Search (if needed)
    # path("search/", views.search, name="search"),

    # Authentication Views
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),

    # Include default Django auth URLs (login, logout, password management)
    path("accounts/", include('django.contrib.auth.urls')),
]