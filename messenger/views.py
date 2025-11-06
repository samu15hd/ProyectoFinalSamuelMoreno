from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

@login_required
def conversacion(request):
    mensajes = Mensaje.objects.filter(
        receptor=request.user
    ) | Mensaje.objects.filter(emisor=request.user)
    mensajes = mensajes.order_by('fecha_envio')

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('conversacion')
    else:
        form = MensajeForm()

    return render(request, 'messenger/conversacion.html', {
        'mensajes': mensajes,
        'form': form
    })

