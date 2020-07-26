from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import os
from django.conf import settings
from .tecban_requests import *
# Create your views here.

tecban_requests = TecbanRequests()

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

def slides(request):
    return render(request, 'slides.html')


def login(request):
    return render(request, "login.html")

def home_c(request):
    amount = 0
    try:
        accounts = tecban_requests.balance_accounts()
    except e:
        pass

    for account in accounts:
        amount += float(account["amount"])
    
    if(amount == 0):
        amount = 23456.78 

    return render(request, "home-c.html", {"amount": amount})

def despesas(request):
    return render(request, "despesas.html")

def metas(request):
    return render(request, "metas.html")

def faq(request):
    return render(request, "faq.html")

def home_p(request):
    return render(request, "home-p.html")

def conta_corrente(request):
    return render(request, "conta-corrente.html")

def inner_page(request):
    return render(request, "inner-page.html")

def plan_mensal(request):
    return render(request, "plan-mensal.html")

def planejamento(request):
    return render(request, "planejamento.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")

def pagamento(request):
    return render(request, "pagamento.html")

def cash_invest(request):
    return render(request, "cash-invest.html")

