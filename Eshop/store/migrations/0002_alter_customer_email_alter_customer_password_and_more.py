# Generated by Django 5.1 on 2024-08-15 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="password",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=60)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="uploads/products/")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.category"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.products"
            ),
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
