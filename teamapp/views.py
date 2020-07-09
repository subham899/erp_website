from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def newabout(request):
    return render(request, 'servicesapp/about.html')

def service(request):
    return render(request, 'service.html')

def portfolio(request):
    return render(request, 'portfolio.html')

