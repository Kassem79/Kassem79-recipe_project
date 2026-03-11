from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Recipes
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),

    # CRUD
    path('create/', views.recipe_create, name='recipe_create'),
    path('update/<int:pk>/', views.recipe_update, name='recipe_update'),
    path('delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),

    # Categories (fixed)
    path('categories/', views.category_list, name='categories'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]