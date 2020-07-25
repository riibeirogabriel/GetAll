from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import os
from django.conf import settings
from .tecban_requests import *
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def accounts(request):
    tecban_requests = TecbanRequests()


    return render(request, str(tecban_requests.consentiment_accounts()))
