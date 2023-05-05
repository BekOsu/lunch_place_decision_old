from django.db import models
from lunch_decision.core.models import Employee
from lunch_decision.restaurants_menus.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()

    class Meta:
        unique_together = ['employee', 'menu']
