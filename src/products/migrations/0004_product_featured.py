# Generated by Django 4.1.3 on 2022-11-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
