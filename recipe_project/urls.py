from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('recipes/', views.recipe_list),
    path('recipe/<int:id>/', views.recipe_detail),
]


