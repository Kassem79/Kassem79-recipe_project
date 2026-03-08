from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, Category
from django.contrib.auth.forms import UserCreationForm

# Home page view
def home(request):
    recipes = Recipe.objects.all()
    breakfast_recipes = recipes.filter(category__name='Breakfast')
    lunch_recipes = recipes.filter(category__name='Lunch')
    dinner_recipes = recipes.filter(category__name='Dinner')
    dessert_recipes = recipes.filter(category__name='Desserts')

    context = {
        'recipes': recipes,
        'breakfast_recipes': breakfast_recipes,
        'lunch_recipes': lunch_recipes,
        'dinner_recipes': dinner_recipes,
        'dessert_recipes': dessert_recipes,
    }
    return render(request, 'home.html', context)

# Recipe list view
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

# Recipe detail view
def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')

# Categories view
def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)   # automatically log user in
            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})