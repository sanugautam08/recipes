from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'base.html')

def recipes(request):
    if request.method=='POST':
        data=request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')
        
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_image=recipe_image
        )

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('searchFood'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('searchFood'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)

def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method=="POST":
        data=request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc

        if recipe_image:
            queryset.recipe_iamge = recipe_image
        queryset.save()
        return redirect('/recipes/')
    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')