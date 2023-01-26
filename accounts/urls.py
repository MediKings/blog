from django.urls import path
from .views import Logout, Register, Login

app_name='accounts'

urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
]