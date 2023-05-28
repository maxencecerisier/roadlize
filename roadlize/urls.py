"""
URL configuration for roadlize project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from service_provider.views_user import UserCreate, CustomAuthToken
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserCreate.as_view(), name='signup'),
    path('signin/', CustomAuthToken.as_view(), name='account_login'),
    path('', include('service_provider.urls')),
]
