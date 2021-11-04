'''
URL de utilities
'''
from django.urls import path


from . import views
from .models import Client,Room


urlpatterns = [
	path('clients/', views.ClientViewSet, name="client"),
	path('rooms/', views.RoomViewSet, name="room"),
	path('bookings/<int:id>', views.BookingViewSet, name="booking"),
	path('bookings/', views.BookingViewSet, name="booking"),
	path('availableRooms/', views.AvailableRoomsViewSet, name="availableRooms"),
	# path('invoices/', views.InvoiceViewSet, name="client"),
    ]
