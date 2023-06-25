from django.db import models
from coordinator.models import Coordinator

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    coordinator=models.ForeignKey(Coordinator,on_delete=models.PROTECT, related_name='events')
    member_count=models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return self.title