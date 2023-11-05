from django.urls import path,include
from vege import views
from vege.models import *

urlpatterns = [
    path('', views.homepage, name="HomePage"),
    path('recipes/', views.recipes, name="recipes"),
    path('view-recipe/<id>/', views.view_recipe, name="view_recipe"),
    path('delete-recipe/<id>/', views.delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/', views.update_recipe, name="update_recipe"),
    path('login/', views.login_page, name="login_page"),
    path('logout/', views.logout_page, name="logout_page"),
    path('register/', views.register, name="register"),
    path('add-recipe/', views.add_recipe, name="add_recipe"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]