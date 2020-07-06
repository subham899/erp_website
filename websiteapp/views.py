from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Customer_info


def home(request):
    return render(request, 'website/index.html')

def newabout(request):
    return render(request, 'website/about.html')

def service(request):
    return render(request, 'website/serviceapp.html')

def portfolio(request):
    return render(request, 'website/portfolio.html')

def team(request):
    return render(request, 'website/team.html')
def contact(request):
    print('sent sucessfully.')
    customer_name = request.POST['name']
    customer_mail = request.POST['email']
    customer_subject =  request.POST['subject']
    customer_messege = request.POST['message']
    Customer = Customer_info(customer_name=customer_name,customer_mail=customer_mail,customer_subject=customer_subject,customer_messege=customer_messege)
    Customer.save('sent')
    return render(request, 'website/index.html')