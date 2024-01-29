from django.urls import path

from kitchen.views import index, CookListView, DishListView,DishTypeListView
urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes-type/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "kitchen"
