from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('г', 'грам'),
        ('кг', 'кілограм'),
        ('мл', 'мілілітр'),
        ('шт', 'штук'),
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    unit = models.CharField(max_length=100, choices=UNIT_CHOICES)
    def __str__(self):
        return self.name
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.author} - {self.recipe}"
    class Meta:
        ordering = ['created_at']

