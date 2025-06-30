from django.shortcuts import render

# Create your views here.

def all_cars_view(request):
	context = {}
	return render(request, 'all_cars.html', context)

def car_details_view(request):
	context = {}
	return render(request, 'car_details.html', context)

def car_category_view(request):
	context = {}
	return render(request, 'car_category.html', context)

def homepage(request):
    return render(request, 'home.html')

def confort_view(request):
    return render(request, 'cars/confort.html')

def lux_view(request):
    return render(request, 'cars/lux.html')

def sport_view(request):
    return render(request, 'cars/sport.html')


def car_details(request, slug):
    cars = {
        'urus': {
            'name': 'Lamborghini Urus',
            'image': 'images/urus.jpg',
            'description': 'Un SUV super sportiv cu motor V8 twin-turbo.'
        },
        'aventador': {
            'name': 'Lamborghini Aventador',
            'image': 'images/aventador.jpg',
            'description': 'Supercar V12, 700 CP, iconic.'
        },
        '488-spyder': {
            'name': 'Ferrari 488 Spyder',
            'image': 'images/488.jpg',
            'description': 'Design italian și performanță pe pistă.'
        },
        'phantom': {
            'name': 'Rolls Royce Phantom',
            'image': 'images/phantom.jpg',
            'description': 'Lux absolut, pentru cei care nu acceptă compromisuri.'
        },
        'cullinan': {
            'name': 'Rolls Royce Cullinan',
            'image': 'images/cullinan.jpg',
            'description': 'SUV-ul suprem în materie de rafinament.'
        },
        'g63': {
            'name': 'Mercedes G63 AMG Brabus',
            'image': 'images/g63.jpg',
            'description': 'Putere și lux off-road.'
        },
        's-class': {
            'name': 'Mercedes S-Class',
            'image': 'images/sclass.jpg',
            'description': 'Confort și tehnologie de vârf.'
        },
        'maybach': {
            'name': 'Mercedes Maybach',
            'image': 'images/maybach.jpg',
            'description': 'Un sedan regal cu toate facilitățile.'
        },
        'bmw-7': {
            'name': 'BMW Seria 7',
            'image': 'images/bmw7.jpg',
            'description': 'Dinamică și eleganță la nivel business.'
        },
    }

    car = cars.get(slug)
    # if not car:
    #     return render(request, 'Cars/car_not_found.html')  # creează opțional o pagină 404 proprie

    return render(request, 'Cars/car_details.html', {'car': car})