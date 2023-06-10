from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ServiceProvider, Service, Booking, Review, Quote
from .serializers import ServiceProviderSerializer, ServiceSerializer, BookingSerializer, ReviewSerializer, QuoteSerializer

class ServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=True, methods=['get'])
    def bookings(self, request, pk=None):
        service_provider = self.get_object()
        bookings = Booking.objects.filter(service_provider=service_provider)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def quotes(self, request, pk=None):
        service_provider = self.get_object()
        quotes = Quote.objects.filter(service_provider=service_provider)
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        service_provider = self.get_object()
        reviews = Review.objects.filter(service_provider=service_provider)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
