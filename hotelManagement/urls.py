"""hotelManagement URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    #v1 Services
    path('v1/api/bookings/', include(('hotelManagement.apps.bookings.url','bookings'),namespace='bookings')),
  
]