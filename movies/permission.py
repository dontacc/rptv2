from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method=='GET':
            return True
        return bool(request.user and request.user.is_staff)

class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET']=['%(app_label)s.view_%(model_name)s']