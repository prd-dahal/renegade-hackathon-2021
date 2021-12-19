from django.urls import path
from .views import members, alert_members

urlpatterns = [
    path('members/', members, name='add-members'),
    path('alert-members/', alert_members, name='alert-members')
]