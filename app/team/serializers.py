from rest_framework import serializers
from .models import Team, TeamMember
# from .validators import validate_team_size


class TeamMemberSerializer(serializers.ModelSerializer):

    team = serializers.CharField(read_only=True)

    # FIXME: validation not working(temp solved in frontend validation)
    def validate_team(self, value):
        count = TeamMember.objects.filter(team_id=value).count()
        if count >= 4:
            raise serializers.ValidationError("Maximum 4 members allowed")
        return value

    def create(self, validated_data):
        return TeamMember.objects.create(team_id=self.context['team_id'],
                                         **validated_data
                                         )

    class Meta:
        model = TeamMember
        fields = ['id', 'team_id', 'team', 'name',]


class TeamSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        leader = self.context['leader']
        return Team.objects.create(leader=leader, **validated_data)

    team_members = TeamMemberSerializer(many=True, read_only=True)
    leader = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'title', 'leader', 'event', 'team_members']
