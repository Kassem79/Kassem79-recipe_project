from django.db import models
from django.contrib.auth.models import User

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Recipe model
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Optional for existing recipes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# Comment model
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.recipe.title}"    