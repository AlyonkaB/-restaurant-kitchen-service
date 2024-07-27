from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_for_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return (
            f"{self.username}: {self.first_name} {self.last_name} "
            f"({self.years_for_experience} years for experience)"
        )


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.price}"
