from django.urls import path, include
from . import views
from .views import user_profile_view
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    # Homepage and Static Pages
    path('', views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Redirect from /accounts/profile to /profile
    path('accounts/profile/', RedirectView.as_view(url='/profile/', permanent=True)),

    # Asset Management Dashboard
    path('asset-dashboard/', views.asset_dashboard_view, name='asset_dashboard'),

    # User Profile and Account Management
    path('profile/', user_profile_view, name='user_profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path("change-password/", views.change_password, name="change_password"),

    # Asset Management
    path("assets/<int:pk>/", views.asset_detail, name="asset_detail"),
    path('assets/', views.asset_list, name='asset_list'),
    path('assets/add/', views.add_asset, name='add_asset'),
    path("assets/<int:pk>/update/", views.asset_update, name="asset_update"),
    path("assets/<int:pk>/delete/", views.asset_delete, name="asset_delete"),

    # Search (if needed)
    # path("search/", views.search, name="search"),

    # Authentication Views
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", views.register, name="register"),

    # Include default Django auth URLs (login, logout, password management)
    path("accounts/", include('django.contrib.auth.urls')),
]