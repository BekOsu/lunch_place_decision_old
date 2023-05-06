from django.db import models
from core.models import RestaurantOwner


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.restaurant.name} : {self.items} - {self.date}"

