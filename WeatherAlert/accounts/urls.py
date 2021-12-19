from django.urls import path
from .views import register, login, logout, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('user-profile/', profile, name='user-profile'),
]