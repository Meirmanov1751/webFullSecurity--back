from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OrderViewSet

router = DefaultRouter()

router.register('order/order', OrderViewSet)
