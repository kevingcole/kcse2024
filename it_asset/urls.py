from django.urls import path
from . import views
from .views import ajax_register

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    path('add/', views.add_asset, name='add_asset'),
    path('add_manufacturer/', views.add_manufacturer, name='add_manufacturer'),
    path('<int:id>/', views.asset_detail, name='asset_detail'),
    path('<int:id>/delete/', views.asset_delete, name='asset_delete'),
    path('<int:pk>/update/', views.asset_update, name='asset_update'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),
    path("ajax_register/", ajax_register, name="ajax_register"),
    path('about/', views.about, name='about'),
]
