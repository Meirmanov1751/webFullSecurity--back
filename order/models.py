from django.db import models

from customer.models import Customer
from product.models import Product
from user.models import User


class Order(models.Model):
    # organization = models.ForeignKey(CommercialOrganization, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order', null=True, blank=True)
    products = models.ManyToManyField(Product)
    description = models.TextField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тапсырыс'
        verbose_name_plural = 'Тапсырыстар'
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.total_amount}'
