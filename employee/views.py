from django.shortcuts import render
from rest_framework import mixins, viewsets
from .permissions import IsSuperAdmin, IsManagementCompany, IsForMany
from .models import Employee
from .serializers import EmployeeSerializer
from .paginations import DocumentPagination


# Create your views here.
class EmployeeViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    pagination_class = DocumentPagination
    serializer_class = EmployeeSerializer
    permission_classes = [IsForMany]
