from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

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


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "kitchen/cook_list.html"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5
