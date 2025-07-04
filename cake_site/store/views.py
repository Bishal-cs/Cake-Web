from django.shortcuts import render

def store(request):
    return render(request, 'store.html')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def order(request):
    return render(request, 'order.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
