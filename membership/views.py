from django.shortcuts import render
from django.http import Http404


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
