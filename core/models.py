from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Dietary Preferences Model
class DietaryPreference(models.Model):
    DIET_CHOICES = [
        ('Vegan', 'Vegan'),
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
    ]
    diet_type = models.CharField(max_length=15, choices=DIET_CHOICES)

    def __str__(self):
        return self.diet_type


# Custom User Model extending AbstractUser
class CustomUser(AbstractUser):
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_group = models.CharField(max_length=10)
    diseases = models.TextField(blank=True, null=True)  # Store any diseases if applicable
    dietary_preference = models.ForeignKey(DietaryPreference, on_delete=models.SET_NULL, null=True, related_name='users')
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')

    def __str__(self):
        return self.username


# Meal Model
class Meal(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]
    name = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=10, choices=MEAL_CHOICES)
    instructions = models.TextField()  # Instructions on how to prepare
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Estimated meal cost

    def __str__(self):
        return self.name


# Ingredient Model
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Price per unit

    def __str__(self):
        return self.name


# MealIngredient Model to associate meals with ingredients
class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)  # Quantity of ingredient used

    def __str__(self):
        return f'{self.meal.name} - {self.ingredient.name}'
