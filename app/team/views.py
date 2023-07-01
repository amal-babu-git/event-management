from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TeamSerializer, TeamMemberSerializer
from .models import Team, TeamMember
from event.models import Event
# Create your views here.


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    def get_queryset(self):
        user = self.request.user
        return Team.objects.prefetch_related('team_members').filter(leader=user.id)

    def create(self, request, *args, **kwargs):
        serializer = TeamSerializer(
            data=request.data,
            context={'leader': self.request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TeamMemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamMemberSerializer

    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    def get_queryset(self):
        return TeamMember.objects.filter(team_id=self.kwargs['team_pk'])

    def get_serializer_context(self):
        super().get_serializer_context()
        return {'team_id': self.kwargs['team_pk']}
