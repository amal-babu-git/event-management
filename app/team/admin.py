from django.contrib import admin
from .models import Team, TeamMember
# Register your models here.


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra: int = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'event',]
    inlines = [TeamMemberInline,]
