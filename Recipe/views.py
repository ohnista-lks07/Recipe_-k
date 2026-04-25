from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from Recipe.models import Recipe
from .forms import RecipeForm, IngredientForm, ReviewForm


def home(request):
    recipes = Recipe.objects.filter(is_public=True)
    return render(request, 'Recipe/home.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.author = request.user
            review.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    return render(request, 'Recipe/recipe_detail.html', {'recipe': recipe, 'form': form})


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'Recipe/recipe_create.html', {'form': form})


@login_required
def recipe_update(request, recipe_id): # редагування
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'Recipe/recipe_update.html', {'form': form})


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if recipe.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'Recipe/recipe_delete.html', {'recipe': recipe})


@login_required
def dashboard(request):
    recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'Recipe/dashboard.html', {'recipes': recipes})


@login_required
def ingredient_add(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, author=request.user)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('ingredient_add', recipe_id=recipe_id)
    else:
        form = IngredientForm()
    return render(request, 'Recipe/ingredient_add.html', {'form': form, 'recipe': recipe})

def review_add(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.author = request.user
            review.save()
            return redirect('review_add', recipe_id=recipe_id)
    else:
        form = ReviewForm()
    return render(request, 'Recipe/review_add.html', {'form': form, 'recipe': recipe})

def register(request):
    if request.user.is_authenticated:   # вже залогований — нема сенсу реєструватись
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Акаунт створено!")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

