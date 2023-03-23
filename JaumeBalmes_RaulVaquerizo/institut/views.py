from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    return render(request, 'index.html')

def prof(request):
    prof = {
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
    context = {'prof': prof}

    return render(request, 'prof.html', context)


def alumn(request):
    alumn = {
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
    context = {'alumn': alumn}
    return render(request, 'alumns.html', context)