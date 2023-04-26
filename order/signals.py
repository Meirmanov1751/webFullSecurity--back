# from .models import Order
# from customer.models import Customer
#
# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# User = get_user_model()
#
# @receiver(post_save, sender=User)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#
# @receiver(post_save, sender=Order)
# def set_customer(sender, instance, created, **kwargs):
#     if created:
#         customer = Customer.objects.get(customer_id=User.id)
#         instance.customer = customer
#         instance.save()
