from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Recipe, Category, Comment
from .forms import RecipeForm, CommentForm

# Home page
def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
        'breakfast_recipes': recipes.filter(category__name='Breakfast'),
        'lunch_recipes': recipes.filter(category__name='Lunch'),
        'dinner_recipes': recipes.filter(category__name='Dinner'),
        'dessert_recipes': recipes.filter(category__name='Desserts'),
    }
    return render(request, 'home.html', context)

# Recipe list
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', {'recipes': recipes})

# Recipe detail with comments
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.recipe = recipe
                comment.author = request.user
                comment.save()
                return redirect('recipe_detail', pk=recipe.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'comments': comments,
        'form': form
    })

# Login / Logout / Signup
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

# Recipe CRUD
def recipe_create(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})

# Categories
def category_list(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.select_related('category').all()
    return render(request, 'categories.html', {'categories': categories, 'recipes': recipes})

# Comments
@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return redirect('recipe_detail', pk=comment.recipe.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=comment.recipe.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # Only the author can delete their comment
    if comment.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    if request.method == "POST":
        comment.delete()
        return redirect('recipe_detail', pk=comment.recipe.pk)

    # Redirect for GET request
    return redirect('recipe_detail', pk=comment.recipe.pk)