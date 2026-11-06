from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "pages/index.html")

def service_details(request):
    return render(request, "pages/service_details.html")

def portfolio_details(request):
    return render(request, "pages/portfolio_details.html")

def starter_page(request):
    return render(request, "pages/starter_page.html")

def form_ok(request):
    return HttpResponse("OK") 