from django.shortcuts import get_object_or_404, render
from .models import Car
# Create your views here.

def all_cars_view(request):
    cars = Car.objects.all()
    return render(request, 'all_cars.html', {'cars': cars})

def car_details_view(request):
	context = {}
	return render(request, 'car_details.html', context)

def category_view(request, category):
    cars = Car.objects.filter(category__iexact=category)
    return render(request, 'Cars/car_category.html', {'cars': cars, 'category': category})


def homepage(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})


def car_details(request, slug):
    car = get_object_or_404(Car, slug=slug)
    return render(request, 'Cars/car_details.html', {'car': car})