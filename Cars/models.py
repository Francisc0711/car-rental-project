from django.db import models

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