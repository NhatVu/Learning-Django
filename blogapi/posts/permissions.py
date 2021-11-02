from rest_framework import permissions

# it will overwrite permission in settings.py
class IsAuthorOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		# read-only permissions are allowed for any request
		if request.method in permissions.SAFE_METHODS:
			return True 
		
		# write permissions are only allowded to the author of a post 
		return obj.author == request.user