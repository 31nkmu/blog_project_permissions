from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    # RETRIEVE, UPDATE, DELETE
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)


class IsCommentOwner(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # RETRIEVE, UPDATE, DELETE
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated and request.user == obj.owner
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)
