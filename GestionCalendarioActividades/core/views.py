from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Evento
# Create your views here.
def index(request):
    EventoS = Evento.objects.all().order_by('-fecha_inicio')
    datos = {
        "Comunicados":Evento,
        
        }
    return render(request, 'core/base.html', datos)