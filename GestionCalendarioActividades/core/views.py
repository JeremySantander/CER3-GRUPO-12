from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Evento
# Create your views here.
def index(request):
    EventoS = Evento.objects.all().order_by('-fecha_inicio')
    filtroSegmento = request.POST.get('FiltrarSegmento')
    if filtroSegmento:
        EventoS = EventoS.filter(segmento=filtroSegmento)
    filtroTipo = request.POST.get('FiltrarTipo')
    if filtroTipo:
        EventoS = EventoS.filter(tipo=filtroTipo)
    datos = {
        "Evento":Evento,
        }
    return render(request, 'core/base.html', datos)