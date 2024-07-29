from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html', {})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html', {})

def main(request):
    return render(request, 'main.html', {})