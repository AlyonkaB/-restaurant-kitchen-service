from django.urls import path

from kitchen.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "kitchen"
