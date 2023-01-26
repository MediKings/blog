from django.urls import path
from .views import Logout, Register, Login

app_name='accounts'

urlpatterns = [
    path('', Login, name='log'),
    path('logout/', Logout, name='logout'),
]