from django.shortcuts   import render
from rest_framework     import viewsets
from core.models        import Evento
from .serializers       import EventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset            = Evento.objects.all()
    serializer_class    = EventoSerializer 
