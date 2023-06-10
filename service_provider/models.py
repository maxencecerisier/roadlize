from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.gis.db import models as gis_model
from django.contrib.gis.geos import Point

class Service(models.Model):
    name = models.CharField(max_length=255, default='Service Name')
    description = models.TextField(default='Service Description')

    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    name = models.CharField(max_length=255, default='Provider Name')
    email = models.EmailField(max_length=255, unique=True, default='provider@example.com')
    phone = models.CharField(max_length=20, default='00-00-00-00-00')
    address = models.CharField(max_length=255, default='Provider Address')
    location = gis_model.PointField(default=Point(0, 0))
    description = models.TextField(default='Provider Description')
    services = models.ManyToManyField(Service)  
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    number_of_ratings = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def calculate_rating(self):
        reviews = self.review_set.all()
        self.rating = sum(review.rating for review in reviews) / reviews.count() if reviews.count() > 0 else 0
        self.number_of_ratings = reviews.count()
        self.save()

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

class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default='Pending')
    price_estimate = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.TextField(default='Quote Description')

@receiver(post_save, sender=Review)
def update_service_provider_rating(sender, instance, **kwargs):
    instance.service_provider.calculate_rating()

@receiver(post_delete, sender=Review)
def update_service_provider_rating_on_delete(sender, instance, **kwargs):
    instance.service_provider.calculate_rating()