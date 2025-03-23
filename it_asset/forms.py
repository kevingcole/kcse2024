from django import forms
from .models import ITAsset, Manufacturer, Employee, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Base form to apply common logic to all forms
class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add 'form-control' class to all fields in the form
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            # Optionally set a default placeholder if label is short enough
            if len(field.label) < 10:  # Adjust this condition as necessary
                field.widget.attrs.update({'placeholder': field.label})

# Get the custom user model
CustomUser = get_user_model()

class ITAssetForm(BaseForm):
    class Meta:
        model = ITAsset
        fields = ['name', 'serial_number', 'manufacturer', 'purchase_date', 'assigned_to']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['manufacturer'].queryset = Manufacturer.objects.all()  # Populate manufacturer dropdown
        self.fields['assigned_to'].queryset = Employee.objects.all()  # Populate assigned_to dropdown

    # Example custom validation for serial number uniqueness
    def clean_serial_number(self):
        serial_number = self.cleaned_data.get("serial_number")
        if ITAsset.objects.filter(serial_number=serial_number).exists():
            raise forms.ValidationError("This serial number is already in use.")
        return serial_number

# Profile form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

    # Example custom validation
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already taken.")
        return email

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

# Manufacturer form
class ManufacturerForm(BaseForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'website']

# Employee form
class EmployeeForm(BaseForm):
    class Meta:
        model = Employee
        fields = ['user', 'department', 'position']