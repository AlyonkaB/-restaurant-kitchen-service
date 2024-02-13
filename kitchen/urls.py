from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    DishListView,
    DishTypeListView,
    DishDetailView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dishes-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
]

app_name = "kitchen"
