from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Ingredient, Dish, Cook


class ModelsTests(TestCase):
    def test_create_user(self):
        username = "Test cook"
        password = "Test123pass"
        test_cook = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        self.assertEqual(test_cook.username, username)
        self.assertTrue(test_cook.check_password(password))

    def test_str_dish_type(self):
        test_dish_type = DishType.objects.create(name="Test dish type")
        self.assertEqual(str(test_dish_type), test_dish_type.name)

    def test_str_ingredient(self):
        test_ingredient = Ingredient.objects.create(name="Test ingredient")
        self.assertEqual(str(test_ingredient), test_ingredient.name)

    def test_str_dish(self):
        test_ingredient = Ingredient.objects.create(name="Test ingredient")
        test_dish_type = DishType.objects.create(name="Test dish type")
        test_cook = get_user_model().objects.create(
            username="Test cook",
            password="Test123pass"
        )
        test_dish = Dish.objects.create(
            name="Test dish",
            description="Test description",
            price=45.34,
            dish_type=test_dish_type,
        )
        test_dish.ingredients.add(test_ingredient)
        test_dish.cooks.add(test_cook)

        self.assertEqual(str(test_dish), f"{test_dish.name} {test_dish.price}")

    def test_str_cook(self):
        test_cook = get_user_model().objects.create_user(
            username="Test cook",
            password="Test123pass"
        )
        self.assertEqual(
            str(test_cook),
            f"{test_cook.username}: {test_cook.first_name} {test_cook.last_name} "
            f"({test_cook.years_for_experience} years for experience)")
