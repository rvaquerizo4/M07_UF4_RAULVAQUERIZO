from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    return render(request, 'index.html')

def prof(request):
    prof = {
        "prof1": {
            "name":"Roger",
            "surname":"Sobrino",
            "age":"17"
        },
        "prof2": {
            "name": "Oriol",
            "surname": "Roca",
            "age": "27"
        },
        "prof3": {
            "name": "Jose Javier",
            "surname": "Faro",
            "age": "13"
        },
    }
    context = {'prof': prof}

    return render(request, 'prof.html', context)


def alumn(request):
    alumn = {
        "alumn1": {
            "name": "Enric",
            "surname": "Marquez",
            "age": "17"
        },
        "alumn2": {
            "name": "Jaume",
            "surname": "Balmes",
            "age": "27"
        },
        "alumn3": {
            "name": "Pedro",
            "surname": "Gaseoso",
            "age": "13"
        },
        "alumn4": {
            "name": "Jorge",
            "surname": "Rosell",
            "age": "17"
        },
        "alumn5": {
            "name": "Josep",
            "surname": "Enric",
            "age": "27"
        },
        "alumn6": {
            "name": "Raul",
            "surname": "Vaquerizo",
            "age": "13"
        },
    }
    context = {'alumn': alumn}
    return render(request, 'alumns.html', context)