# Generated by Django 4.1.3 on 2022-11-29 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_description_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product", name="summary", field=models.TextField(),
        ),
    ]
