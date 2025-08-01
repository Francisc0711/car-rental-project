from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Car, Reservation
from .forms import ReservationForm
from django.utils.dateparse import parse_date
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

    pickup_date = request.GET.get("pickup_date")
    dropoff_date = request.GET.get("dropoff_date")

    if pickup_date and dropoff_date:
        pickup_date = parse_date(pickup_date)
        dropoff_date = parse_date(dropoff_date)

        reserved_cars = Reservation.objects.filter(
            start_date__lte=dropoff_date,
            end_date__gte=pickup_date
        ).values_list("car_id", flat=True)

        cars = cars.exclude(id__in=reserved_cars)

    return render(request, "home.html", {"cars": cars})




@login_required
def car_details(request, slug):
    car = get_object_or_404(Car, slug=slug)
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if end_date < start_date:
                messages.error(request, "End date cannot be before start date!")
            else:
                overlap = Reservation.objects.filter(
                    car=car,
                    start_date__lte=end_date,
                    end_date__gte=start_date
                ).exists()

                if overlap:
                    messages.error(request, "The car is already reserved for the selected dates.")
                else:
                    Reservation.objects.create(user=request.user, car=car, start_date=start_date, end_date=end_date)
                    messages.success(request, f"Reservation for {car.brand} {car.model} has been made!")
                    return redirect("profile")

    return render(request, "Cars/car_details.html", {"car": car, "form": form})