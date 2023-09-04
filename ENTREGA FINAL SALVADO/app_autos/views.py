from django.shortcuts import render, get_object_or_404
from .models import Coche
from .forms import CocheForm

def listar_coches(request):
    coches = Coche.objects.all()
    return render(request, 'app_autos/listar_coches.html', {'coches': coches})

def ver_coche(request, coche_id):
    coche = get_object_or_404(Coche, pk=coche_id)
    return render(request, 'app_autos/ver_coche.html', {'coche': coche})

def buscar_coches(request):
    query = request.GET.get('q')
    coches = Coche.objects.filter(modelo__icontains=query)
    return render(request, 'app_autos/listar_coches.html', {'coches': coches})


