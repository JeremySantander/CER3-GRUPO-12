from rest_framework import routers
from .serializers import EventoSerializer
from django.urls import path , include
from .views import EventoViewSet

router = routers.DefaultRouter()
router.register('evento',EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]