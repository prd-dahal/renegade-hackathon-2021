"""WeatherAlert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, temp_home, dashboard, compare
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = "Weather Alert"
from accounts import urls as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # pradeep's start
    path('FloodAssessment/', include("FloodAssessment.urls", namespace="FloodAssessment")),
    #pradeep's end

    #utsav's start
    path('accounts/', include("accounts.urls")),
    path('alerts/', include("alert.urls")),
    path('temp-home/', temp_home, name='temp-home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('compare/', compare, name='compare'),

    #utsav's end

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
