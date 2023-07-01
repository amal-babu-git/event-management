from django.core.exceptions import ValidationError
from .models import TeamMember


def validate_team_size(team_id):
    count = TeamMember.objects.filter(team_id=team_id).count()

    if count >= 2:
        raise ValidationError("Team size is 7 members")
