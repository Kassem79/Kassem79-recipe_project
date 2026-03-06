from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipes/', views.recipe_list),
    path('recipe/<int:id>/', views.recipe_detail),
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("categories/", views.categories, name="categories"),
]


