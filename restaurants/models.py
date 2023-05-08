from django.db import models
from UserAuth.models import Profile


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

