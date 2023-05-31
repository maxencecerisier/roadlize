from rest_framework_gis.fields import GeometryField
from rest_framework import serializers
from .models import ServiceProvider, Service, Booking, Review

class ServiceProviderSerializer(serializers.ModelSerializer):
    location = GeometryField()

    class Meta:
        model = ServiceProvider
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
