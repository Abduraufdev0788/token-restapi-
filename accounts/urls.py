from django.urls import path
from .views import Register, Login, Logout, Profile, PasswordChangeView, AdminPanelView, ManagmentView, UserView

urlpatterns = [
    path('auth/register/', Register.as_view()),
    path('auth/login/', Login.as_view()),
    path('auth/logout/', Logout.as_view()),
    path('auth/profile/', Profile.as_view()),
    path('auth/change-password/', PasswordChangeView.as_view()),
    
    path("admin-panel/", AdminPanelView.as_view()),
    path("management/", ManagmentView.as_view()),
    path("public/", UserView.as_view()),
]
