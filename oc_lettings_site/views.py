from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def error_404_view(request, exception=None):
    return render(request, '404.html')


def error_500_view(request, exception=None):
    return render(request, '500.html')