from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_restaurant_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    class Meta:
        abstract = True


class RestaurantOwner(Profile):
    pass
    # Add any other fields specific to restaurant owners


class Employee(Profile):
    pass
    # Add any other fields specific to employees
