from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Cook, Ingredient, Dish, DishType


class TestPublic(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        urls = [
            "kitchen:cook-list",
            "kitchen:dish-list",
            "kitchen:dish-type-list",
            "kitchen:ingredient-list"
        ]
        for url in urls:
            res = self.client.get(reverse(url))
            self.assertNotEqual(res.status_code, 200)


class TestPrivate(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="test_username1",
            password="test123Pass"
        )

        self.user2 = get_user_model().objects.create_user(
            username="test_username2",
            password="test123Pass"
        )

        self.client.force_login(self.user1)

    def test_retrieve_ingredient(self):
        Ingredient.objects.create(
            name="test_ingredient1"
        )
        Ingredient.objects.create(
            name="test_ingredient2"
        )
        response = self.client.get(reverse("kitchen:ingredient-list"))
        self.assertEqual(response.status_code, 200)
        ingredients = Ingredient.objects.all()
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredients)
        )

    def test_retrieve_dish_type(self):
        DishType.objects.create(
            name="test_dish_type1"
        )
        DishType.objects.create(
            name="test_dish_type2"
        )
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )

    def test_retrieve_cook(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )

    def test_retrieve_dish(self):
        test_ingredient = Ingredient.objects.create(name="Test ingredient")
        test_dish_type = DishType.objects.create(name="Test dish type")

        test_dish = Dish.objects.create(
            name="Test dish",
            description="Test description",
            price=45.34,
            dish_type=test_dish_type,
        )
        test_dish.ingredients.add(test_ingredient)
        test_dish.cooks.add(self.user1)

        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
