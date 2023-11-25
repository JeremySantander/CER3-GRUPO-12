from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Evento, Segmento
# Create your views here.
def index(request):
    EventoS = Evento.objects.all().order_by('-fecha_inicio')
    datos = {
        "Comunicados":Evento,
        "Entidades":Segmento.objects.all()
        }
    return render(request, 'core/base.html', datos)