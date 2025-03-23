from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ITAsset, Manufacturer, Employee, Profile, Asset
from .forms import ITAssetForm, ManufacturerForm, EmployeeForm, CustomUserCreationForm, RegistrationForm, ProfileForm
from django.contrib.auth import login, get_user_model, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()

# Registration View
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect("home")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})

# Asset List View
def asset_list(request):
    assets = Asset.objects.all()
    manufacturers = Manufacturer.objects.all()
    employees = Employee.objects.all()
    context = {
        'assets': assets,
        'manufacturers': manufacturers,
        'employees': employees,
    }
    return render(request, 'assets/asset_list.html', context)

# Add Asset View
def add_asset(request):
    if request.method == 'POST':
        form = ITAssetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Asset created successfully!")
            return redirect('asset_list')
    else:
        form = ITAssetForm()

    manufacturers = Manufacturer.objects.all()
    employees = Employee.objects.all()

    return render(request, 'assets/add_asset.html', {
        'form': form,
        'manufacturers': manufacturers,
        'employees': employees,
    })

# Asset Detail View
@login_required
def asset_detail(request, pk):
    asset = get_object_or_404(ITAsset, pk=pk)
    return render(request, 'assets/asset_detail.html', {'asset': asset})

# User Profile View
@login_required
def user_profile_view(request):
    return render(request, 'profile/user_profile.html', {'user': request.user})

# Home View
def home(request):
    return render(request, 'asset_list.html')

# About View
def about(request):
    return render(request, 'about.html')

# Contact View
def contact(request):
    return render(request, 'contact.html')

# Asset Dashboard View (Optional)
def asset_dashboard_view(request):
    # Example: you might want to show asset statistics or an overview here
    asset_count = ITAsset.objects.count()
    manufacturer_count = Manufacturer.objects.count()
    employee_count = Employee.objects.count()
    
    context = {
        'asset_count': asset_count,
        'manufacturer_count': manufacturer_count,
        'employee_count': employee_count,
    }
    
    return render(request, 'asset_dashboard.html', context)

# Profile Edit View
@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/profile_edit.html', {'form': form})

# Change Password View
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Keep the user logged in after password change
            messages.success(request, "Password changed successfully!")
            return redirect('user_profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

# Asset Update View
@login_required
def asset_update(request, pk):
    asset = get_object_or_404(ITAsset, pk=pk)
    if request.method == 'POST':
        form = ITAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            messages.success(request, "Asset updated successfully!")
            return redirect('asset_list')
    else:
        form = ITAssetForm(instance=asset)
    return render(request, 'assets/asset_update.html', {'form': form})

# Asset Delete View
@login_required
def asset_delete(request, pk):
    asset = get_object_or_404(ITAsset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        messages.success(request, "Asset deleted successfully!")
        return redirect('asset_list')
    return render(request, 'assets/asset_delete.html', {'asset': asset})