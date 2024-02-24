from rest_framework import generics, permissions 
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm
from .forms import ManualCarForm
from .forms import CarFileForm
from .models import Car, Provider
from .serializers import ProviderSerializer, CarSerializer 

# Create your views here.

def home(request):
    cars = Car.objects.all()
    content = {'cars' : cars}
    return render(request, 'base/homepage.html', content)

def customer(request, pk):
    car = None
    for i in Car.objects.all():
        if i['car_id'] == int(pk):
            car = i
            
    context = {'car' : car}
    return render(request, 'base/car.html', context)

def addCar(request):
    form = CarForm()
    if request.method == "POST":
        print(request.POST)
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        print("Request wasn't POST")
        
    context = {'form':form}
    return render(request, 'base/car_form.html', context)

def updateCar(request, pk):
    car = Car.objects.get(car_id=pk)
    form = CarForm(instance=car)
    
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        print("Request wasn't POST")
        
    context = {'form':form}
    return render(request, 'base/car_form.html', context)

def deleteCar(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('home')
    else:
        print("Request wasn't POST")
        
    return render(request, 'base/delete.html', {'obj': car})


# REST API
class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows provider to be viewed or edited.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    
class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer