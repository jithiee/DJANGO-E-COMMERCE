from django.db import models
# Create your models here.


class Vehicle(models.Model):
    MAKE_CHOICES= [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('Chevrolet', 'Chevrolet'),
        ('Nissan', 'Nissan'),
        ('BMW', 'BMW'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Audi', 'Audi'),
        ('Volkswagen', 'Volkswagen'),
        # Add more brands here
    ]

    def __str__(self):
        return f"{self.year} {self.make} - {self.transmission}"
    
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        ('CVT', 'CVT'),
        # Add more transmission choices here
    ]
    
    make = models.CharField(max_length=50,choices=MAKE_CHOICES)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField() 
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    car_img = models.ImageField(upload_to='vehicle_images/')  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_available = models.BooleanField(default=True)
    description = models.TextField(max_length=500, blank=True)
    # booking_date = models.DateTimeField( auto_now=True, auto_now_add=False)
    # return_date =  models.DateTimeField( auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return f"  {self.make}   {self.transmission} {self.year} "
    

    
    
    
 