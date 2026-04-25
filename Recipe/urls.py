from django.urls import path
from . import  views
urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'), #
    path('recipe/create/', views.recipe_create, name='recipe_create'), #
    path('recipe/update/<int:recipe_id>/', views.recipe_update, name='recipe_update'), # редагування
    path('recipe/delete/<int:recipe_id>/', views.recipe_delete, name='recipe_delete'), # видалення
    path('dashboard/', views.dashboard, name='dashboard'), # ваші рецепти, тільки залоговані
    path('recipe/<int:recipe_id>/ingredients/', views.ingredient_add, name='ingredient_add'), #додавання інгредієнтів
    path('recipe/<int:recipe_id>/review/', views.review_add, name='review'),
    path('register/', views.register, name='register'),

]
