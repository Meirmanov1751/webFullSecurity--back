from django.shortcuts import render
from rest_framework import mixins, viewsets
from .permissions import IsSuperAdmin, IsManagementCompany, IsCustomer, IsExecutive, IsForMany
from .models import Product
from .serializers import ProductSerializer, ProductListSerializer
from .paginations import DocumentPagination


# Create your views here.
class ProductViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    pagination_class = DocumentPagination
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        elif self.request.method == 'POST':
            return ProductSerializer
        else:
            return ProductSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsForMany]
        elif self.action == 'create':
            permission_classes = [IsExecutive]
        else:
            permission_classes = [IsExecutive]
        return [permission() for permission in permission_classes]
