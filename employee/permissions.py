from rest_framework.permissions import BasePermission


class IsManagementCompany(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'management_company'


class IsExecutive(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role == 'executor')
        return request.user.role == 'executor'


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'super_admin' or request.user.role == 'auditor' or request.user.role == 'customer'


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        print(request.user.role == 'super_admin')
        return request.user.role == 'super_admin' or request.user.role == 'super_admin'


class IsForMany(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'super_admin' or request.user.role == 'customer' or request.user.role == 'executor' \
            or request.user.role == 'management_company' or request.user.role == 'auditor'
