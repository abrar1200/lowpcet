from django.urls import path
from . import views

app_name = 'meals'  # Namespace for the meals app

urlpatterns = [
    path('', views.meal_list, name='meals'),  # Ensure `views.meal_list` exists
]

