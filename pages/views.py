from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import PageForm
from django.contrib import messages
from django.views.generic import ListView
from .models import Page
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def crear_pagina(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            pagina = form.save(commit=False)
            pagina.autor = request.user  # 👈 Asignamos el autor
            pagina.save()
            messages.success(request, "Página creada con éxito.")
            return redirect('listar_paginas')
    else:
        form = PageForm()
    return render(request, 'pages/crear_pagina.html', {'form': form})

class PageListView(ListView):
    model = Page
    template_name = 'pages/listado_paginas.html'
    context_object_name = 'paginas'

def about(request):
    return render(request, 'pages/about.html')

from django.shortcuts import render
from .models import Page

def listar_paginas(request):
    paginas = Page.objects.order_by('-fecha_creacion')
    return render(request, 'pages/listado_paginas.html', {'paginas': paginas})

from django.shortcuts import get_object_or_404

def detalle_pagina(request, id):
    pagina = get_object_or_404(Page, id=id)
    return render(request, 'pages/detalle_pagina.html', {'pagina': pagina})

@login_required
def editar_pagina(request, id):
    pagina = get_object_or_404(Page, id=id)

    if pagina.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para editar esta página.")

    if request.method == 'POST':
        form = PageForm(request.POST, instance=pagina)
        if form.is_valid():
            form.save()
            messages.success(request, "Página actualizada correctamente.")
            return redirect('detalle_pagina', id=pagina.id)
    else:
        form = PageForm(instance=pagina)

    return render(request, 'pages/editar_pagina.html', {
        'form': form,
        'pagina': pagina
    })

@login_required
def eliminar_pagina(request, id):
    pagina = get_object_or_404(Page, id=id)
    if pagina.autor != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar esta página.")

    if request.method == 'POST':
        pagina.delete()
        messages.success(request, "Página eliminada correctamente.")
        return redirect('listar_paginas')

    return render(request, 'pages/confirmar_eliminacion.html', {'pagina': pagina})

@login_required
def mis_paginas(request):
    paginas = Page.objects.filter(autor=request.user).order_by('-fecha_creacion')
    return render(request, 'pages/mis_paginas.html', {'paginas': paginas})





