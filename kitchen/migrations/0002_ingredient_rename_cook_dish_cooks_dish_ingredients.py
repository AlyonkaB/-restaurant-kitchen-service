# Generated by Django 5.0.1 on 2024-01-20 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.RenameField(
            model_name="dish",
            old_name="cook",
            new_name="cooks",
        ),
        migrations.AddField(
            model_name="dish",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="dishes", to="kitchen.ingredient"
            ),
        ),
    ]
