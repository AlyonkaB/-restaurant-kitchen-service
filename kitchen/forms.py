from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from kitchen.models import Dish, Ingredient, Cook


class DishCreateForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_for_experience")

    def clean_years_for_experience(self):
        return validate_years_for_experience(self.cleaned_data["years_for_experience"])


def validate_years_for_experience(
    years_for_experience):
    if not years_for_experience.isdigit():
        raise ValidationError("The field can only contain numbers")
    elif not 0 < years_for_experience < 100:
        raise ValidationError("The value of years of experience cannot be more than 100, and be less than 0")
    return years_for_experience