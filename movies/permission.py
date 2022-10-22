from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        # return bool(request.user and request.user.is_staff)
    # def has_permission(self, request, view):
    #     pass
    #     # return bool(
    #     #     # request.method == permissions.SAFE_METHODS
    #     #     # or
    #     #     # request.user.is_staff
    #     # )
