# Uncomment the following imports before adding the Model code

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
CAR_BODY_TYPE = (
    ('suv', 'SUV'),
    ('sedan', 'Sedan'),
    ('Hatchback', 'Hatchback'),
    ('Convertible', 'Convertible'),
    ('Pickup', 'Pickup'),
    ('Coupe', 'Coupe'),
    ('Minivan', 'Minivan'),
)


class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)

    # Create a toString method for object string representation
    def __str__(self):
        return self.name + " " + self.description


class CarModel(models.Model):
    # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=200, choices=CAR_BODY_TYPE, default='SUV')
    year = models.IntegerField(default=2023,
                               validators=[
                                   MaxValueValidator(2023),
                                   MinValueValidator(2015)
                               ])

# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
