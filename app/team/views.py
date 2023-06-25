from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TeamSerializer, TeamMemberSerializer
from .models import Team, TeamMember
# Create your views here.


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer