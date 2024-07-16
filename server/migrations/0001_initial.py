# Generated by Django 5.0.7 on 2024-07-16 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Rice', 'Rice'), ('Noodle', 'Noodle'), ('Dish', 'Dish'), ('Baking', 'Baking'), ('Hotpot', 'Hotpot'), ('Soup', 'Soup'), ('Drink', 'Drink'), ('Other', 'Other')], max_length=10)),
                ('description', models.TextField()),
                ('preparation_time', models.SmallIntegerField()),
                ('cooking_time', models.SmallIntegerField()),
                ('likes', models.PositiveIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instruction', to='server.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=5)),
                ('unit', models.CharField(max_length=50)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='server.recipe')),
            ],
        ),
    ]
