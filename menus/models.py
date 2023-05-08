from django.db import models
from restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line

    def __str__(self):
        return f"{self.restaurant.name} : {self.items} - {self.date}"