from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import os
from django.conf import settings
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
    headers = {
        "x-fapi-financial-id":"c3c937c4-ab71-427f-9b59-4099b7c680ab",
        "x-fapi-interaction-id": "15bbc01f-f883-4e91-88c6-b26245b9a35b",
        "Authorization": "fefa1b6c-90ab-4422-a59d-54fe2fcf12f2"
    }
    print(settings.BASE_DIR, flush=True)
    print(type(settings.BASE_DIR), flush=True)
    TRANSPORT_CERT_KEY = os.path.join(str(settings.BASE_DIR), "client_private_key.key")
    TRANSPORT_CERT = os.path.join(str(settings.BASE_DIR), "client_certificate.crt")
    client = (TRANSPORT_CERT, TRANSPORT_CERT_KEY)
    response = requests.get(
        "https://rs1.tecban-sandbox.o3bank.co.uk/open-banking/v3.1/aisp/accounts",
        headers=headers,
        verify=False,
        cert=client)

    return render(request, str(response.json()))
