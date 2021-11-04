from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.transaction import atomic
from django.db import transaction
from .models import Client,Room,Booking,BookingRoom,Payment,Invoice
from rest_framework.response import Response
from .serializers import ClientMSerializer,RoomSerializer,BookingRoomSerializer,BookingSerializer,InvoiceSerializer,PaymentSerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Q

@api_view(['GET','POST'])
def ClientViewSet(request,*args,**kwargs):
    if request.method == 'GET':
        clients = Client.objects.all()
        data = []
        for client in clients:
            serializer = ClientMSerializer(client)
            data.append(serializer.data)
    if request.method == 'POST':
        serializer = ClientMSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save() # saving Cliente instance
            data = serializer.data
            
    return Response(data)



@api_view(['GET','POST'])
def RoomViewSet(request,*args,**kwargs):
    if request.method == 'GET':
        rooms = Room.objects.all()
        data = []
        for room in rooms:
            serializer = RoomSerializer(room)
            data.append(serializer.data)
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            data = serializer.data
    return Response(data)


@api_view(['GET'])
def AvailableRoomsViewSet(request,*args,**kwargs):
    if request.method == 'GET':

        bookedRooms = BookingRoom.objects.filter(
            (Q(inicial_date__range=(request.query_params.get('inicial_date'),request.query_params.get('final_date'))) | 
            Q(final_date__range=(request.query_params.get('inicial_date'),request.query_params.get('final_date')))) & 
            ~Q(status=3)
        )#occupated dates
        rooms = Room.objects.all()
        rooms = rooms.exclude(id__in=bookedRooms.values('booking'))
        
        data = []
        for room in rooms:
            serializer = RoomSerializer(room)
            data.append(serializer.data)
    return Response(data)



@atomic
@api_view(['GET','POST','PATCH'])
def BookingViewSet(request,*args,**kwargs):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        if id in kwargs:
            bookings = bookings.filter(id=kwargs['id'])
        data = []
        for book in bookings:
            serializer = BookingSerializer(book)
            booked_rooms = BookingRoom.objects.filter(booking=serializer.data['id'])
            completeObj = serializer.data
            # import pdb; pdb.set_trace()
            completeObj['rooms'] = []
            for booked_room in booked_rooms:
                booked_room_serialized = BookingRoomSerializer(booked_room)
                completeObj['rooms'].append(booked_room_serialized.data)
            # completeObj['rooms'] = booked_rooms
            data.append(completeObj)
    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            booking = serializer.data #I got the id of the booking
            # import pdb; pdb.set_trace()
            objRooms = []
            data = booking
            for room in request.data['rooms']:
                objRoom = room
                print(booking)
                # import pdb; pdb.set_trace()
                objRoom['booking'] = booking['id'] 
                booking['rooms'] = []
                booked_room_serializer = BookingRoomSerializer(data=objRoom)
                if booked_room_serializer.is_valid():
                    booked_room_serializer.save()
                    booking['rooms'].append(booked_room_serializer.data)
                else:
                    transaction.set_rollback(True) 
                    raise ValidationError(booked_room_serializer.errors)
            data = booking
    elif request.method == 'PATCH':
        if kwargs['id'] is not None:
            booking = Booking.objects.get(id=kwargs['id'])
            booking.status = request.data['status']
            booking.save()
            data = BookingSerializer(booking).data
        else:
            pass
    return Response(data)


@api_view(['GET','POST'])
def InvoiceViewSet(request,*args,**kwargs):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        data = []
        for invoice in invoices:
            serializer = InvoiceSerializer(invoice)
            data.append(serializer.data)
    if request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            data = serializer.data
    return Response(data)

@api_view(['GET','POST','DELETE'])
def PaymentViewSet(request,*args,**kwargs):
    if request.method == 'GET':
        payments = Payment.objects.all()
        data = []
        for payment in payments:
            serializer = PaymentSerializer(payment)
            data.append(serializer.data)
    if request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            data = serializer.data
    return Response(data)
