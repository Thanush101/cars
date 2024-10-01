from django.shortcuts import render, redirect
from .models import Car
from .form import CarForm


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list') 
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def cars_home(request):
    context = {
        'title': 'Welcome to Cars Home',
        'message': 'Explore our collection of cars!'
    }
    return render(request, 'index.html', context)

def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})

from django.shortcuts import render, get_object_or_404
from .models import Car

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})



# def remove_car(request):




# Create your views here.