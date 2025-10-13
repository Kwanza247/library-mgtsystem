from rest_framework import permissions

class IsLibrarian(permissions.BasePermission):
    """
    Allow only librarians to create, update, or delete books.
    """
    def has_permission(self, request, view):
        # Only librarians can add/edit/delete; others can read
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and getattr(request.user, "role", None) == "librarian"
