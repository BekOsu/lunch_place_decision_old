from django.db import models
from core.models import Employee
from restaurants_menus.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()

    class Meta:
        unique_together = ['employee', 'menu']
