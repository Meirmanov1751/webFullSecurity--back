from django.shortcuts import render
from requests import Response
from rest_framework import mixins, viewsets
from .permissions import IsForMany, IsCustomer
from .models import Order
from .serializers import OrderSerializer, OrderListSerializer
from .paginations import DocumentPagination


# Create your views here.
class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    pagination_class = DocumentPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderListSerializer
        elif self.request.method == 'POST':
            return OrderSerializer
        else:
            return OrderSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsForMany]
        elif self.action == 'create':
            permission_classes = [IsCustomer]
        else:
            permission_classes = [IsCustomer]
        return [permission() for permission in permission_classes]
