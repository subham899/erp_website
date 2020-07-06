from django.shortcuts import render

def home(request):
    return render(request, 'aboutapp/aboutapp.html')

def service(request):
    return  render(request, 'aboutapp/serviceapp.html')

def portfolio(request):
    return render(request, 'aboutapp/portfolio.html')