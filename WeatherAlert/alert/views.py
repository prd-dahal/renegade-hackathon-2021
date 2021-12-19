from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MembersForm, AlertForm
from .models import MembersModels, AlertModel
import json

# alert email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.


def members(request):
    form = MembersForm()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        location = request.POST['location']
        user = request.user
        member = MembersModels.objects.create(name=name, email=email, phone_number=phone_number, location=location,
                               user=user)
        return redirect('dashboard')
    with open('data/location.json') as location_file:
        data = json.load(location_file)['locations']
    context = {
        "form": form,
        "data": data,
    }

    return render(request, 'alert/members.html', context)


def alert_email(request, alerter, email, user):
    current_site = get_current_site(request)
    mail_subject = 'High Flood Risk Alert'
    message = render_to_string('alert/alert_email.html', {
        'alerter': alerter,
        'domain': current_site,
        'user': user,
    })
    to_email = email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()


def alert_members(request):
    form = AlertForm()
    if request.method == 'POST':
        location = request.POST['location']
        river_level = request.POST['river_level']
        
        #checks for the river level
        if(int(river_level)<10):
             return redirect('dashboard')
        
        user = request.user
        members = MembersModels.objects.filter(user=user, location=location)
        print(members)
        members_list = list()
        for member in members:
            members_list.append(member.name)
            alert_email(request, member.user, member.email, member)

        alert_members = AlertModel.objects.create(location=location,
                                                  river_level=river_level,
                                                  members=members_list)
        alert_members.save()
        return redirect('dashboard')
    # user = request.user
    # email = user.email
    # alert_email(request, user, email)
    with open('data/location.json') as location_file:
        data = json.load(location_file)['locations']


    context = {
        "form": form,
        "data": data,
    }
    return render(request, 'alert/alert_form.html', context)


