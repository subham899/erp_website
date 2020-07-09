from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def service(request):
    return render(request, 'website/serviceapp.html')

def newabout(request):
    return render(request, 'servicesapp/about.html')
