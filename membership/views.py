from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    return render(request, 'membership/index.html')

def about(request):
    return render(request, 'membership/about.html')

def events(request):
    return render(request, 'membership/events.html')

def members(request):
    return render(request, 'membership/members.html')

def contact(request):
    return render(request, 'membership/contact.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Succesfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'membership/login.html', {'form': form})
