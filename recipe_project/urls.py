from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),

    path('create/', views.recipe_create, name='recipe_create'),
    path('update/<int:pk>/', views.recipe_update, name='recipe_update'),
    path('delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),

    path('categories/', views.categories, name='categories'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]