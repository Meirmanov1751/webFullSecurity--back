from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from requests import Response

from employee.models import Employee
from customer.models import Customer
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from djoser.signals import user_registered

User = get_user_model()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'customer':
            customer_profile = Customer.objects.create(customer=instance)
            instance.is_active = True
            instance.profile = customer_profile
            instance.profile.save()
        elif instance.role == 'executor':
            employee_profile = Employee.objects.create(executor=instance)
            instance.is_active = True
            instance.profile = employee_profile
            instance.profile.save()


@receiver(post_save, sender=User)
def activate_user(sender, instance=None, created=False, **kwargs):
    if created:
        instance.is_active = True
        instance.save()


@receiver(user_registered)
def activate_user_registered(sender, user, request, **kwargs):
    user.is_active = True
    user.save()
