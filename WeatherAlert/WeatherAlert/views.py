from django.shortcuts import render
from django.http import HttpResponse
from alert.models import MembersModels


def home(request):
    return render(request, 'home.html')


def temp_home(request):
    return render(request, 'includes/base.html')


def dashboard(request):
    user = request.user
    members = MembersModels.objects.filter(user = user)
    context = {
        "members": members,
    }
    return render(request, 'dashboard.html', context)


def compare(request):
    return render(request, 'compare.html')