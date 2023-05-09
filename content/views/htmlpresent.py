from django.shortcuts import render, HttpResponse, get_object_or_404
from content.models import Portfolio, Contacts, Service, OurClients, MainPageDigits, Testimonal


def present(request):
    portfolios=Portfolio.objects.all()
    contacts=Contacts.objects.all()
    services=Service.objects.all()
    pagedigits=MainPageDigits.objects.all()
    testimonals=Testimonal.objects.all()
    ourClients=OurClients.objects.all()
    return render(request, 'index.html',
                  {'portfolios':portfolios,'contacts':contacts,'services':services,
                   'pagfeDigits':pagedigits,'testimonals':testimonals,'ourClients':ourClients})


def all_services(request):
    services=Service.objects.all()
    return render(request,'all_services.html',{'services':services})

def all_portfolios(request):
    portfolios=Portfolio.objects.all()
    services=Service.objects.all()
    return render(request,'all_portfolios.html',{'services':services,'portfolios':portfolios})

def service_get(request,pk):
    service=get_object_or_404(Service.objects.all(),pk=pk)
    services=Service.objects.all()
    return render(request,'service_detail.html',{'services':services,'service':service})

def portfolio_get(request,pk):
    portfolio=get_object_or_404(Portfolio.objects.all(),pk=pk)
    services=Service.objects.all()
    return render(request,'portfolio_details.html',{'services':services,'portfolio':portfolio})




def privacy_policy(request):
    services=Service.objects.all()
    return render(request,'privacy_policy.html',{'services':services})