# from rest_framework.permissions import BasePermission
#
# class IsManagementCompany(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'management_company'
#
# class IsExecutive(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'executive'
#
# class IsCustomer(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'customer'
#
# class IsSuperAdmin(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.role == 'super_admin'