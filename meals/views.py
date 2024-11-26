from django.shortcuts import render

def meal_list(request):
    return render(request, 'meals/meal_list.html')  # Ensure this template exists

# Create your views here.
