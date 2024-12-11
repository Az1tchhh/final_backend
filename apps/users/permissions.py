from rest_framework.permissions import IsAuthenticated


class IsWebUser(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return hasattr(request.user, 'web_user')