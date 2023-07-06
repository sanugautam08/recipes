from django.urls import path,include
from vege import views
from vege.models import *

urlpatterns = [
    path('', views.homepage, name="HomePage"),
    path('recipes/', views.recipes, name="recipes"),
    path('delete-recipe/<id>/',views.delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/',views.update_recipe, name="update_recipe"),
]