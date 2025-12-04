from django.urls import path
from .views import Register, Login, Logout

urlpatterns = [
    path('auth/register/', Register.as_view()),
    path('auth/login/', Login.as_view()),
    path('auth/logout/', Logout.as_view()),
]
