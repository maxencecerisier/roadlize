from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ServiceProviderViewSet, ServiceViewSet, BookingViewSet, ReviewViewSet, QuoteViewSet

router = DefaultRouter()
router.register(r'service_providers', ServiceProviderViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
