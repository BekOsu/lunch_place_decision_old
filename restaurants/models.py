from django.db import models
from core.models import Profile


class RestaurantOwner(Profile):

    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(RestaurantOwner, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.owner)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    items = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line

    def __str__(self):
        return f"{self.restaurant.name} : {self.items} - {self.date}"
