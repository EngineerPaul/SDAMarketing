# Generated by Django 4.1.4 on 2023-01-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_costgroup_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cost",
            name="cost",
            field=models.TextField(max_length=63, verbose_name="Стоимость"),
        ),
        migrations.AlterField(
            model_name="cost",
            name="term",
            field=models.TextField(max_length=31, verbose_name="Срок"),
        ),
        migrations.AlterField(
            model_name="cost",
            name="title",
            field=models.TextField(max_length=255, verbose_name="Название услуги"),
        ),
    ]
