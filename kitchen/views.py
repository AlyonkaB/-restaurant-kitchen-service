from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType, Ingredient


def index(request: HttpRequest) -> HttpResponse:
    cooks = Cook.objects.count()
    dish = Dish.objects.count()
    diss_type = DishType.objects.count()
    ingredient = Ingredient.objects.count()
    context = {
        "cooks": cooks,
        "dish": dish,
        "diss_type": diss_type,
        "ingredient": ingredient
    }
    return render(request, "kitchen/index.html", context=context)
