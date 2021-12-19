from django.urls import path
from . import views
app_name = "FloodAssessment"
urlpatterns= [

    path('', views.machineLearning, name='machineLearning'),
]