# Generated by Django 3.2 on 2023-05-07 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_restaurant_owner', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurantowner')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('items', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]
