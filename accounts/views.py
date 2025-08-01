from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from Cars.models import Reservation


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully, you can log in right now!.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            messages.error(request, "Username sau parolă incorectă.")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def profile_view(request):
    rezervari = Reservation.objects.filter(user=request.user)  
    return render(request, "accounts/profile.html", {"rezervari": rezervari})

@login_required
def cancel_reservation(request, res_id):
    rezervare = get_object_or_404(Reservation, id=res_id, user=request.user)
    rezervare.delete()
    messages.success(request, "Rezervarea a fost anulată cu succes.")
    return redirect("profile")