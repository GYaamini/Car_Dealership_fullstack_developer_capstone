from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name + "," + self.description


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('EV', 'Electric Vehicle'),
        ('SPORTS CAR', 'Sports Car'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('MINIVAN', 'Minivan'),
        ('COUPE', 'Coupe'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=CAR_TYPES)
    year = models.IntegerField(
                                default=2024,
                                validators=[
                                    MaxValueValidator(2025),
                                    MinValueValidator(2015)
                                ]
                            )

    def __str__(self):
        return self.name
