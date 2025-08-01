from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Car(models.Model):
    category = models.CharField(max_length=100, default="")
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.car.slug}"