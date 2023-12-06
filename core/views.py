from django.shortcuts import render, redirect
from django.views.generic import View
from .models import TallerMecanico
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CitaForm
from .models import Cita
from django.contrib import messages

@login_required
def lista_talleres(request):
    talleres = TallerMecanico.objects.all()
    return render(request, 'lista_talleres.html', {'talleres': talleres})

@login_required
def detalle_taller(request, taller_id):
    taller = get_object_or_404(TallerMecanico, pk=taller_id)
    return render(request, 'informacion_taller.html', {'taller': taller})

class Contacto(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chat.html', context = {})

@login_required
def programar_cita(request):
    form = CitaForm()
    citas = Cita.objects.all()

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            nueva_cita= form.save() 
            return redirect('lista_talleres') 

    talleres = TallerMecanico.objects.all()
    context = {'form': form, 'talleres': talleres, 'citas': citas}

    messages.success(request, 'Tu cita ha sido programada con éxito.')

    return render(request, 'programar_cita.html', context)


