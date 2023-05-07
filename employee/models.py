from django.db import models
from user.models import User


# Create your models here.
class Employee(models.Model):
    executor = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True,related_name="executor")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Орындаушы'
        verbose_name_plural = 'Орындаушылар'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.executor}'