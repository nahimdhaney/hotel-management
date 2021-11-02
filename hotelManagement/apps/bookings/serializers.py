"""
Field's Serializers
"""

from rest_framework import serializers
from hotelManagement.apps.bookings.models import Client,Room


class ClientMSerializer(serializers.ModelSerializer):
    """Client serializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        model = Client
        fields = '__all__'

class RoomMSerializer(serializers.ModelSerializer):
    """Client serializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        model = Room
        fields = '__all__'
