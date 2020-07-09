from django.shortcuts import render

def home(request):
    return render(request, 'servicesapp/index.html')

def newabout(request):
    return render(request, 'servicesapp/about.html')

def portfolio(request):
    return render(request, 'servicesapp/portfolio.html')

def contact(request):
    return render(request, 'servicesapp/contact_app.html')

def team(request):
    return render(request, 'servicesapp/team.html')