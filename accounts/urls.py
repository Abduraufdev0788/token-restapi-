from django.urls import path
from .views import Register

urlpatterns = [
    path('auth/register/', Register.as_view())
]
