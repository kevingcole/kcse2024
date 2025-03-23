# it_asset/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    # Add custom fields if necessary
    pass

class ITAsset(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

# Employee Model
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=15, default='First Name')
    last_name = models.CharField(max_length=15, default='Surname')
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username


# Signals to create and save profile
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        pass


# Employee Model
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"


# Manufacturer Model
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


# IT Asset Model
class ITAsset(models.Model):
    def validate_purchase_date(value):
        if value > timezone.now().date():
            raise ValidationError("Purchase date cannot be in the future.")

    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True, blank=True)
    purchase_date = models.DateField(validators=[validate_purchase_date])
    assigned_to = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


# Asset Model (linked to ITAsset)
class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    it_asset = models.OneToOneField('ITAsset', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name