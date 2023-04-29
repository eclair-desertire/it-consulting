from django.shortcuts import render
from content.models import Portfolio, Contacts, Service


def present(request):
    return render(request, 'index.html')