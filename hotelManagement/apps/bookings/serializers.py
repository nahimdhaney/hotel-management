"""
Field's Serializers
"""

from rest_framework import serializers
from hotelManagement.apps.bookings.models import Client,Room,Booking,BookingRoom,Invoice
from .models import Client,Room,Booking,BookingRoom
from django.db.models import Q

class ClientMSerializer(serializers.ModelSerializer):
    """Client serializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        model = Client
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    """Client serializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    """Client serializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        model = Booking
        fields = '__all__'


class BookingRoomSerializer(serializers.ModelSerializer):
    """Client serializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        model = BookingRoom
        fields = '__all__'
    def validate(self, data):
        """
        Check that the rooms are not booked by anyone else
        
        """
        # import pdb; pdb.set_trace()
        if BookingRoom.objects.filter(
            (Q(inicial_date__range=(data['inicial_date'],data['final_date'])) | 
            Q(final_date__range=(data['inicial_date'],data['final_date']))) & 
            Q(room=data['room'])).exists():
            # .format(2*(height + width),height*width)
            raise (serializers.ValidationError(
                "Room nro {} is occupied between dates {} and {}".
                format(data['room'],data['inicial_date'],data['final_date'])
            ))
        return data

