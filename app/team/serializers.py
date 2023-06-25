from rest_framework import serializers
from .models import Team, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['name', 'team']


class TeamSerializer(serializers.ModelSerializer):
    team_members = TeamMemberSerializer(many=True,read_only=True)

    class Meta:
        model = Team
        fields = ['title', 'leader', 'event', 'team_members']
