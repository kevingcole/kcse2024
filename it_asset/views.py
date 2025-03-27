from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import ITAsset, Manufacturer, Employee, Profile
from .forms import ITAssetForm, RegistrationForm, ProfileForm, AssetForm, ManufacturerForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from it_asset.models import ITAsset
import sys
import io

# Registration View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save user without committing to DB yet
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Set the first name and last name manually if they're included in the form
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            # Create an Employee record (can include defaults for other fields)
            Employee.objects.create(
                user=user,
                phone_number="N/A",  # Default value
                address="N/A",  # Default value
                position="New Hire",  # Default value
                department="Unassigned"  # Default value
            )

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Asset List View with Pagination
@login_required
def asset_list(request):
    assets = ITAsset.objects.all().order_by('id')
    paginator = Paginator(assets, 8)  # Show 10 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    manufacturers = Manufacturer.objects.all()
    employees = Employee.objects.all()

    context = {
        'page_obj': page_obj,
        'manufacturers': manufacturers,
        'employees': employees,
    }

    return render(request, 'assets/asset_list.html', context)

# Add Asset View
@login_required
def add_asset(request):
    if request.method == 'POST':
        print("Form submitted")
        form = AssetForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            messages.success(request, "Asset created successfully!")
            return redirect('asset_list')
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)  # Print form errors to the console for debugging
            print("Form data:", form.cleaned_data)  # Print form data to the console for debugging
            messages.error(request, "Error creating asset. Please check the form for errors.")
    else:
        form = AssetForm()
    return render(request, 'assets/add_asset.html', {'form': form})

# Asset Detail View
@login_required
def asset_detail(request, id):
    asset = get_object_or_404(ITAsset, id=id)
    return render(request, 'assets/asset_detail.html', {'asset': asset})

# User Profile View
@login_required
def user_profile(request):
    profile = request.user.profile  # Fetch the user's profile
    return render(request, 'profiles/profile.html', {'profile': profile})

# Home View
@login_required
def home(request):
    return render(request, 'home.html')

# About View
def about(request):
    return render(request, 'about.html')

# Contact View
def contact(request):
    return render(request, 'contact.html')

# Asset Dashboard View
@login_required
def asset_dashboard_view(request):
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
    profile = request.user.profile  # Fetch the user's profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)  # Bind the form to the POST data and the profile instance
        if form.is_valid():
            form.save()  # Save the changes to the profile
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')  # Redirect to the profile page
        else:
            print(form.errors)  # Debugging: Print form errors to the console
            messages.error(request, "Error updating profile. Please check the form for errors.")
    else:
        form = ProfileForm(instance=profile)  # Pre-fill the form with the current profile data
    return render(request, 'profiles/profile_edit.html', {'form': form})

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
from django.shortcuts import render, get_object_or_404, redirect
from .models import ITAsset, Manufacturer, Employee
from django.contrib import messages

@login_required
def asset_update(request, id):
    asset = get_object_or_404(ITAsset, id=id)
    manufacturers = Manufacturer.objects.all()  # Fetch all manufacturers
    employees = Employee.objects.all()  # Fetch all employees

    if request.method == 'POST':
        asset.name = request.POST.get('name')
        asset.serial_number = request.POST.get('serial_number')
        asset.manufacturer_id = request.POST.get('manufacturer')
        asset.assigned_to_id = request.POST.get('assigned_to')
        asset.save()
        messages.success(request, "Asset updated successfully!")
        return redirect('asset_detail', id=asset.id)

    return render(request, 'assets/asset_update.html', {
        'asset': asset,
        'manufacturers': manufacturers,
        'employees': employees,
    })

# Asset Delete View
@login_required
def asset_delete(request, id):
    asset = get_object_or_404(ITAsset, id=id)
    if request.method == 'POST':
        asset.delete()
        messages.success(request, "Asset deleted successfully!")
        return redirect('asset_list')
    return render(request, 'assets/asset_confirm_delete.html', {'asset': asset})

# Logout View
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'it_asset/logout.html')

@login_required
def profile(request):
    return render(request, 'it_asset/profile.html')

@login_required
def add_manufacturer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        website = request.POST.get('website')  # Get the website field from the form
        if name:
            Manufacturer.objects.create(name=name, website=website)  # Save the website field
            messages.success(request, "Manufacturer added successfully!")
            return redirect('asset_list')
        else:
            messages.error(request, "Name is required.")
    return render(request, 'assets/add_manufacturer.html')

# AJAX Register View
@csrf_exempt
def ajax_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password1 != password2:
            return JsonResponse({"success": False, "error": "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "error": "Username already taken."})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Log in the user immediately after registering
        user = authenticate(username=username, password=password1)
        if user:
            login(request, user)
            return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Invalid request."})

""" from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings """

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Capture email output if using the console backend
        email_output = io.StringIO()
        sys.stdout = email_output  # Redirect console output

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['your-email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            sys.stdout = sys.__stdout__  # Reset console output
            email_sent_message = email_output.getvalue()

            messages.success(request, f"Your message has been sent successfully! 📩\n\nConsole Output:\n{email_sent_message}")

        except Exception as e:
            sys.stdout = sys.__stdout__  # Reset console output
            messages.error(request, f"Error sending message: {e}")

        return redirect("contact")

    return render(request, "contact.html")