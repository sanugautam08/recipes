from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_desc = models.TextField()
    recipe_image = models.ImageField(upload_to="recipeImg")

    def __str__(self):
        return self.recipe_name
