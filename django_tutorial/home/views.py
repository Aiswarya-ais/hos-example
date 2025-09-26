from django.shortcuts import render
from django.http import HttpResponse
from .models import departments,doctors  

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctor(request):
    dict_doc = {
        'doc': doctors.objects.all()   
    }
    return render(request, 'doctors.html', dict_doc)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dep = {
        'dept': departments.objects.all()  
    }
    return render(request, 'department.html', dict_dep)
