from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')

@login_required(login_url="/login/")
def add_recipe(request):
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
    return render(request,'add_recipe.html')

def recipes(request):
    queryset = Recipe.objects.all()
    total = len(queryset)

    if request.GET.get('searchFood'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('searchFood'))

    context = {'recipes': queryset, 'total':total}
    return render(request, 'recipes.html', context)

def view_recipe(request,id):
    context = {}
    return render(request, 'view_recipe.html', context)

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
    return render(request, 'login.html')

@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account successfully created.")
        return redirect('/register/')
    
    return render(request, 'register.html')