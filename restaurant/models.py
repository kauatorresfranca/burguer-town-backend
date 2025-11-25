from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    opening_hours = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

