from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

profesores = {
        "prof1": {
            "id": "1",
            "name":"Roger",
            "surname":"Sobrino",
            "age":"17"
        },
        "prof2": {
            "id": "2",
            "name": "Oriol",
            "surname": "Roca",
            "age": "27"
        },
        "prof3": {
            "id": "3",
            "name": "Jose Javier",
            "surname": "Faro",
            "age": "13"
        },
    }
alumnos = {
        "alumn1": {
            "id": "1",
            "name": "Enric",
            "surname": "Marquez",
            "age": "17"
        },
        "alumn2": {
            "id": "2",
            "name": "Jaume",
            "surname": "Balmes",
            "age": "27"
        },
        "alumn3": {
            "id": "3",
            "name": "Pedro",
            "surname": "Gaseoso",
            "age": "13"
        },
        "alumn4": {
            "id": "4",
            "name": "Jorge",
            "surname": "Rosell",
            "age": "17"
        },
        "alumn5": {
            "id": "5",
            "name": "Josep",
            "surname": "Enric",
            "age": "27"
        },
        "alumn6": {
            "id": "6",
            "name": "Raul",
            "surname": "Vaquerizo",
            "age": "13"
        },
    }
def index(request):
    return render(request, 'index.html')

def profs(request):
    prof = profesores
    context = {'prof': prof}
    return render(request, 'profs.html', context)


def alumns(request):
    alumn = alumnos
    context = {'alumn': alumn}
    return render(request, 'alumns.html', context)

def alumn(request, pk):
    alumn_Obj = None
    for i in alumnos.values():
        if i['id'] == pk:
            alumn_Obj = i
            break
    return render(request, 'alumn.html', {'alumn': alumn_Obj})


def prof(request, pk):
    prof_Obj = None
    for i in profesores.values():
        if i['id'] == pk:
            prof_Obj = i
            break
    return render(request, 'prof.html', {'prof': prof_Obj})
