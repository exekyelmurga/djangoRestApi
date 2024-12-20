from rest_framework import routers
from .api import ModelosViewSet

router = routers.DefaultRouter()

router.register('api/modelos', ModelosViewSet, 'modelos')

urlpatterns = router.urls