from django.shortcuts import render
import datetime

# Create your views here.

def menu(request):
    return render(request,'book/menu.html')

def index(request):
    return render(request,'book/index.html')
    
    
def book(request):
    return render(request,'book/books.html')

def obtener_fecha(request):
    fecha_actual = datetime.datetime.now()
    return render(request,'book/fecha.html',{'fecha':fecha_actual})

def palindromo(request,name):
    return render(request,'book/palindro.html',{'name': name})
