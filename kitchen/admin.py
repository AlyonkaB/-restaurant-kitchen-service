from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Dish, Cook, Ingredient


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price"]
    search_fields = ["name"]
    list_filter = ["name", "dish_type"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_for_experience",)
    fieldset = UserAdmin.fieldsets + ((
                                          "info",
                                          {"fields": ("years_for_experience",)}
                                      ),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_for_experience",
                    "email",
                )
            },
        ),
    )


admin.site.register(Ingredient)
admin.site.register(DishType)
