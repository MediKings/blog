from django.urls import path
from .views import Logout, Register, Login


urlpatterns = [
    path('', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
]