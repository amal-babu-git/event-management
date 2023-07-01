from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    coordinator=serializers.StringRelatedField()
    class Meta:
        model=Event
        fields=['id','title','description','coordinator','member_count']