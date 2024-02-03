from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    CookDetailView,
    DishListView,
    DishTypeListView)


urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes-type/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "kitchen"
