from django.test import TestCase

from kitchen.forms import CookCreationForm


class FormTests(TestCase):
    def test_cook_creation_form(self):
        test_data = {
            "username": "test_user_name",
            "password1": "Pass12345",
            "password2": "Pass12345",
            "email": "test@mail.com",
            "first_name": "test_name",
            "last_name": "test_last_name",
            "years_for_experience": 45,
        }

        form = CookCreationForm(data=test_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, test_data)

