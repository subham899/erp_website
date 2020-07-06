from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def service(request):
    return  render(request, 'service.html')

def newabout(request):
    return render(request, 'about.html')
