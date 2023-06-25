from rest_framework_nested import routers
from .views import EventViewSet

# Event endpoint
router = routers.DefaultRouter()
router.register('', viewset=EventViewSet, basename='events')



urlpatterns = router.urls 
