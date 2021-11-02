'''
URL de utilities
'''
from django.urls import path


from . import views
from .models import Client


urlpatterns = [
	path('clients/', views.ClientViewSet, name="client"),
    ]
