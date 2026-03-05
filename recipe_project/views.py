from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

# def home_page_view(request):
#    return HttpResponse("<h1>Recipe, project</>")
def home(request):
    recipes = Recipe.objects.all()[:6]
    return render(request, 'home.html', {'recipes': recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
