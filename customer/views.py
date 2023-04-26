from django.shortcuts import render
from rest_framework import mixins, viewsets
from .permissions import IsSuperAdmin, IsManagementCompany, IsForMany
from .models import Customer
from .serializers import CustomerSerializer
from .paginations import DocumentPagination


# Create your views here.
class CustomerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    pagination_class = DocumentPagination
    serializer_class = CustomerSerializer
    permission_classes = [IsForMany]
