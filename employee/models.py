from django.db import models
from core.models import Employee
from restaurants.models import Menu


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} voted {self.points} points for {self.menu}"
