from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from . models import Event
from .serializers import EventSerializer

# Create your views here.


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    http_method_names = ['get', 'post',
                         'options', 'headers']

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return [IsAdminUser()]
        return super().get_permissions()
