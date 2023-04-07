from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone

class Vehicle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_reg_no = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now)
    
    
    
    def __str__(self):
        return self.vehicle_reg_no

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)

class Trip(models.Model):
    journey_Choices = (
            ('Nairobi', 'Nairobi'),
            ('Thika', 'Thika'),
            ('Malaa', 'Malaa'),
            ('Makongeni', 'Makongeni'),
            
     )
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    odometer_start=models.PositiveIntegerField()
    odometer_close=models.PositiveIntegerField()
    journey_start=models.CharField(max_length=100, choices=journey_Choices) 
    journey_destination=models.CharField(max_length=100, choices=journey_Choices) 
    amount_collected=models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    
    class Meta:
        ordering = ('-created',) 
    def __str__(self):
        return f'Trip for {self.Vehicle.vehicle_reg_no}'
    

    def total_amount_collected(self):
     return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']    
        #  return Trip.objects.filter(Vehicle=self.Vehicle).aggregate(Sum('amount_collected'))['amount_collected__sum']
        # return Trip.objects.filter(Vehicle=self.Vehicle, Vehicle__owner=request.user).aggregate(Sum('amount_collected'))['amount_collected__sum']



class Expense(models.Model):
    Expense_Choices = (
            ('FUEL-DIESEL', 'Fuel-Diesel'),
            ('BREAKFAST', 'Breakfast'),
            ('Lunch', 'Lunch'),
            ('Salaries', 'Salaries'),
            ('Parking Fee', 'Parking Fee'),
            ('Line', 'Line'),
            ('Boys', 'Boys'),
            ('Car Wash', 'Car Wash'),
            ('Oil/CC', 'Oil/CC'),
            ('Puncher', 'Puncher'),
            ('BREAKFAST', 'Breakfast'),
            ('Services', 'Services'),
            ('Greasing', 'Greasing'),
            ('Pad', 'Pad'),
            ('Garage', 'Garage'),
            ('Spare', 'Spare'),
            ('Tyre', 'Tyre'),
            ('Batteries', 'Batteries'),
            ('Break Fluid', 'Break Fluid'),
            ('Others', 'Others'),
        )   
     
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=Expense_Choices) 
    amount_incurred=models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def total_expense_incurred(self):
        return Expense.objects.aggregate(Sum('amount_incurred'))['amount_incurred__sum'] 

    def __str__(self):
        return f'Expense for {self.Vehicle.vehicle_reg_no}'
    
