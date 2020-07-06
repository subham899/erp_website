from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def erp_mail(request):
    template = render_to_string('contact_app/index.html',{})

    if request.method== "POST":
        erp_name = request.POST['name']

        erp_massege = request.POST['message']


        #SEND MAIL
        send_mail(
            'NEW ERP WEBSITE',
            erp_massege,
            settings.EMAIL_HOST_USER,
            ['subhambasu980@gmail.com'],
            fail_silently=False,
        )

        return render(request, 'contact_app/index.html', {'erp_name': erp_name})
    else:
        return render(request, 'contact_app/index.html')

