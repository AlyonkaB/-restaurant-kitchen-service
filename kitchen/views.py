from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishCreateForm, CookCreationForm, CookUpdateForm, \
    SearchDishIngredientDishTypeForm, SearchCookForm
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


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "kitchen/cook_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        context["search_form"] = SearchCookForm()
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = SearchCookForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
            return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes")

class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"
    queryset = Dish.objects.all().prefetch_related("ingredients").select_related("dish_type")
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["search_form"] = SearchDishIngredientDishTypeForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().prefetch_related("cooks")

class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        context["search_form"] = SearchDishIngredientDishTypeForm()
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = SearchDishIngredientDishTypeForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
            return queryset


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "kitchen/ingredient_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context["search_form"] = SearchDishIngredientDishTypeForm()
        return context

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        form = SearchDishIngredientDishTypeForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
            return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/ingredient_delete_form.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_delete_form.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishCreateForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishCreateForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen/dish_delete_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    template_name = "kitchen/cook_form.html"
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "kitchen/cook_delete_form.html"
    success_url = reverse_lazy("kitchen:cook-list")
