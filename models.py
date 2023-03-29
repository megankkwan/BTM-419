from django.db import models

class Sale(models.Model):
    car_dealership = models.CharField(max_length=100)
    daily_sales = models.IntegerField()
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)

class Claim(models.Model):
    number_of_claims = models.IntegerField()