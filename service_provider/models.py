from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Service(models.Model):
    name = models.CharField(max_length=255, default='Service Name')
    description = models.TextField(default='Service Description')

    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    name = models.CharField(max_length=255, default='Provider Name')
    email = models.EmailField(max_length=255, unique=True, default='provider@example.com')
    phone = models.CharField(max_length=20, default='000-000-0000')
    address = models.CharField(max_length=255, default='Provider Address')
    description = models.TextField(default='Provider Description')
    services = models.ManyToManyField(Service)  
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    number_of_ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.service_provider.name} - {self.service.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    comment = models.TextField(default='Review Comment')

    def __str__(self):
        return f"{self.user.username} - {self.service_provider.name} - {self.rating}"
