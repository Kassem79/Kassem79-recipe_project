from django.urls import path
from import views
from .views import home_page_view


urlpatterns = [
    path('', views.home),
    path('recipes/', views.recipe_list),
    path('recipe/<int:id>/', views.recipe_detail),
]


