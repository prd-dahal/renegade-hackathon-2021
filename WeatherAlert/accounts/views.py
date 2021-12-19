from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm, UserProfileForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        "form": form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        print(email)
        print(password)
        # user = Account.objects.get(email=email, password=password)

        user = auth.authenticate(email=email, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You are now logged out!")
    return redirect('login')


def profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('user-profile')

    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'user_form': form,
    }

    return render(request, 'accounts/profile.html', context)
