from django.conf.urls import url
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Booking,BookingRoom,Client, Room
from rest_framework.test import APIRequestFactory,APIClient
from pprint import pprint

# importing datetime module
import datetime
 
import json

class BookingAPITestCase(APITestCase):
    """Booking API test case."""

    def setUp(self):
        """Test case setup."""
        self.client_db = Client.objects.create(
            nit='9020353',
            comercial_name='Nahim Terrazas Parada',
            invoice_name='Mi Empresa SRL',
            email='nahimdhaney@hotmail.com'
        )
        self.room_db = Room.objects.create(
            number='A3',
            price=64
        )
        self.booking_db = Booking.objects.create(
            client = self.client_db
        )
        d = datetime.date(2021,11,2)
        d2 = datetime.date(2021,11,3)
        self.room_booked_id = BookingRoom.objects.create(
            inicial_date= d,
            final_date=d2,
            room=self.room_db,
            booking=self.booking_db
        )

        # URL
        self.url_booking = '/v1/api/bookings/bookings/'
        self.url_client = '/v1/api/bookings/clients/'



    def test_response_success(self):
        """Verify request succeed."""
        client_api = APIClient()
        self.assertEqual(client_api.get(self.url_client, follow=True).status_code, status.HTTP_200_OK)

    def test_response_one(self):
        """Verify request that only exist one element."""
        client_api = APIClient()
        response =client_api.get(self.url_client, follow=True)
        print(len(json.loads(response.content)))
        self.assertEqual(len(json.loads(response.content)),1)
    
    def test_booking(self):
        """test one Booking accepted."""
        client_api = APIClient()
        objBooking = {"client":self.client_db.id,"rooms":[{"room":self.room_db.id,"inicial_date":"2021-11-08","final_date":"2021-11-08"}]}
        response =client_api.post(self.url_booking,objBooking,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_not_same_day(self):
        """Booking should only accept 1."""
        client_api = APIClient()
        objBooking = {"client":self.client_db.id,"rooms":[{"room":self.room_db.id,"inicial_date":"2021-11-02","final_date":"2021-11-02"}]}
        response =client_api.post(self.url_booking,objBooking,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
