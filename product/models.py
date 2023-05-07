from django.db import models

from employee.models import Employee
from user.models import User



class Product(models.Model):
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='product', null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Өнім'
        verbose_name_plural = 'Өнімдер'
        ordering = ['name']

    def __str__(self):
        return self.name
