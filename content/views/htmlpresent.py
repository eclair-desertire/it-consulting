from django.shortcuts import render


def present(request):
    return render(request, 'index.html')