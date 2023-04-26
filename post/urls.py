from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet

router = DefaultRouter()

router.register('posts/posts', PostViewSet)
