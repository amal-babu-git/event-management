from rest_framework import serializers
from .models import Team, TeamMember


class TeamMemberSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return TeamMember.objects.create(team_id=self.context['team_id'], **validated_data)

    team = serializers.CharField(read_only=True)

    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'team']


class TeamSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        leader = self.context['leader']
        return Team.objects.create(leader=leader, **validated_data)

    team_members = TeamMemberSerializer(many=True, read_only=True)
    leader = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'title', 'leader', 'event', 'team_members']
