from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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


class CookDetailView(generic.DetailView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 9


class IngredientListView(generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "kitchen/ingredient_list.html"
    paginate_by = 9


class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_delete_form.html"
