from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def error_404_view(request, exception=None):
    return render(request, '404.html')


def error_500_view(request, exception=None):
    return render(request, '500.html')

def trigger_error(request):
    division_by_zero = 1 / 0