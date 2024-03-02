from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishDetailView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView
)


urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    # path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    # path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dishes-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dishes-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dishes-delete"),
    path("dishes-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes-type/create/", DishTypeCreateView.as_view(), name="dishes-type-create"),
    path("dishes-type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dishes-type-update"),
    path("dishes-type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dishes-type-delete"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete")
]

app_name = "kitchen"
