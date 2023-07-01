from rest_framework_nested import routers
from .views import TeamViewSet, TeamMemberViewSet

# team endpoint
router = routers.DefaultRouter()
router.register('', viewset=TeamViewSet, basename='teams')

# team member endpoint ,nested 
team_router = routers.NestedDefaultRouter(
    parent_router=router, parent_prefix='', lookup='team')
team_router.register(prefix='members', viewset=TeamMemberViewSet,
                     basename='team-members')

urlpatterns = router.urls + team_router.urls
