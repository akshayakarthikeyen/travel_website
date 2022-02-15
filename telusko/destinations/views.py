from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hyderabad(request):
    return render(request ,'Hyderabad.html')
    return redirect('login')

def Pune(request):
    return render(request , 'Pune.html')
    return redirect('login')

def Mumbai(request):
    return render(request , 'Mumbai.html')
    return redirect('login')

def Banglore(request):
    return render(request, 'Banglore.html')
    return redirect('login')

def booking(request):
    return render(request , 'booking.html')
