from django.contrib.auth.models import AbstractUser
from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    nutritional_info = models.TextField()

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from core.models import DietaryPreference  # Adjust this import based on where DietaryPreference is defined

class Meal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    nutritional_info = models.TextField()

class CustomUser(AbstractUser):
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_group = models.CharField(max_length=10)
    diseases = models.TextField(blank=True, null=True)  # Store any diseases if applicable
    dietary_preference = models.ForeignKey(DietaryPreference, on_delete=models.SET_NULL, null=True, related_name='users_users')
    groups = models.ManyToManyField(
        Group,
        related_name='users_user_set',  # Specify a unique related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users_user_set_permissions',  # Specify a unique related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username

# Create your models here.
