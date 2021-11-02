from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Client
from rest_framework.response import Response
from .serializers import ClientMSerializer

@api_view(['GET','POST','PUT'])
def ClientViewSet(request):
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
    if request.method == 'PUT':
        client = Client.objects.get(id=request.data['id'])
        user = User.objects.get(id=request.data['user'])
        serializer = ClientMSerializer(client, data=request.data)
        user_serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True) and user_serializer.is_valid(raise_exception=True):
            serializer.save() # saving Cliente instance
            user_serializer.save()
            data = serializer.data
            
    return Response(data)
