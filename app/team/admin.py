from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Team, TeamMember
# Register your models here.


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    # fields=['id','name']
    extra: int = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'event',]
    inlines = [TeamMemberInline,]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'team']
