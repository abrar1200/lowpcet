
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Meal
from django.core.exceptions import ObjectDoesNotExist

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def profile(request):
    return render(request, 'core/profile.html')

def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        user = request.user  # Get the logged-in user
        try:
            # Fetch meals based on the user's dietary preference
            if user.dietary_preference:
                meals = Meal.objects.filter(meal_type=user.dietary_preference.diet_type)
            else:
                meals = Meal.objects.all()  # Show all meals if no preference is set
        except ObjectDoesNotExist:
            # Handle case where dietary preference doesn't exist (for any reason)
            meals = Meal.objects.all()  # Fallback to showing all meals
    else:
        # If the user is not authenticated, show all meals or a generic selection
        meals = Meal.objects.all()  # Show all meals to unauthenticated users

    return render(request, 'core/home.html', {'meals': meals})

def meals(request):
    return render(request, 'core/meals.html')
def meals(request):
    # You can customize this to display a list of meals or any other content related to meals
    meals = Meal.objects.all()  # Example, you can filter meals based on user preferences
    return render(request, 'core/meals.html', {'meals': meals})
def meal_detail(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    return render(request, 'core/meal_detail.html', {'meal': meal})
# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # If the form is valid, log the user in
            user = form.get_user()
            login(request, user)
            return redirect('core:home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('core:home')  # Redirect to home page after logout
