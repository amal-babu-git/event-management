from django.db import models
from django.conf import settings
from event.models import Event
# Create your models here.


class Team(models.Model):
    title = models.CharField(max_length=50, unique=True)
    leader = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name='teams')

    def __str__(self) -> str:
        return self.title


class TeamMember(models.Model):
    # id = models.BigAutoField(validators=[validate_team_size])
    name = models.CharField(max_length=100, null=True, blank=True)
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             related_name='team_members',)

    def __str__(self) -> str:
        return self.name
