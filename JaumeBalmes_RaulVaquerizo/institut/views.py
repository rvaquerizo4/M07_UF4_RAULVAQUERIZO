from django.shortcuts import render, redirect
from .forms import AlumForm, ProfForm
from django.http import HttpResponse
from django.template import loader, Context
from django.template.context import RequestContext

from .models import Alum, Prof

from django.shortcuts import render, redirect
from .forms import AlumForm, ProfForm
from django.http import HttpResponse
from django.template import loader, Context
from django.template.context import RequestContext

from .models import Alum, Prof


def index(request):
    return render(request, 'index.html')


def profs(request):
    prof = Prof.objects.all()
    context = {'prof': prof}
    return render(request, 'profs.html', context)


def alumns(request):
    alumn = Alum.objects.all()
    context = {'alumn': alumn}
    return render(request, 'alumns.html', context)


def alumn(request, pk):
    alumn_Obj = Alum.objects.get(id=pk)
    return render(request, 'alumn.html', {'alumn': alumn_Obj})


def prof(request, pk):
    prof_Obj = Prof.objects.get(id=pk)
    return render(request, 'prof.html', {'prof': prof_Obj})


def form_alum(request):
    form = AlumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alumns')

    context = {'form': form}
    return render(request, 'form_alum.html', context)


def form_prof(request):
    form = ProfForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profs')
    context = {'form': form}
    return render(request, 'form_prof.html', context)


def update_alumn(request, pk):
    alumn = Alum.objects.get(id=pk)
    form = AlumForm(request.POST or None, instance=alumn)

    if form.is_valid():
        form.save()
        return redirect('alumns')

    context = {'form': form}
    return render(request, 'form_alum.html', context)


def update_prof(request, pk):
    prof = Prof.objects.get(id=pk)
    form = ProfForm(request.POST or None, instance=prof)

    if form.is_valid():
        form.save()
        return redirect('profs')

    context = {'form': form}
    return render(request, 'form_prof.html', context)
