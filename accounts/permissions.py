from rest_framework.permissions import BasePermission

class Is_Admin(BasePermission):
    message = 'siz amdin emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    

class Is_Managment(BasePermission):
    message = "siz meneger emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    
class Is_User(BasePermission):
    message = "siz usersiz !!! "

    def has_permission(self, request, view):
        return request.user and request.user.is_user
    